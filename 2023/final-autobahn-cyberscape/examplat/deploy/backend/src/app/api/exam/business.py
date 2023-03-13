"""Business logic for /auth API endpoints."""
from http import HTTPStatus
import yaml
import os
import json

from flask import current_app, jsonify
from flask_restx import abort
from app.util.loader import FullLoader, SafeLoader
from werkzeug.utils import secure_filename
from app.models.question import Question
from app.util.util import remove_duplicate, validate_yaml
from app import db
from app.api.auth.decorators import token_required, teacher_token_required
from app.models.exam import Exam

@teacher_token_required
def process_exam_creation_request(name, limit, question):
    user_id = process_exam_creation_request.public_id
    if Exam.find_by_name(name):
        abort(HTTPStatus.CONFLICT, f"Exam with the same name is already exist.", status="fail")
    
    new_exam = Exam(exam_name=name, time_limit=limit, question_file=question, created_by=user_id)    
    db.session.add(new_exam)
    db.session.commit()
    response = jsonify(
        status="success",
        message="successfully created",
    )
    response.status_code = HTTPStatus.CREATED
    response.headers["Cache-Control"] = "no-store"
    response.headers["Pragma"] = "no-cache"
    return response

@teacher_token_required
def delete_exam(exam_id):
    user_id = delete_exam.public_id
    exam = Exam.find_by_exam_id(exam_id)
    filename = exam.question_file
    os.unlink(os.path.join(current_app.config.get("UPLOAD_PATH"), filename))
    Exam.delete_if_exist(exam_id, user_id)
    db.session.commit()
    response = jsonify(
        status="success",
        message="successfully deleted",
    )
    response.status_code = HTTPStatus.OK
    response.headers["Cache-Control"] = "no-store"
    response.headers["Pragma"] = "no-cache"
    return response

@teacher_token_required
def publish_exam(exam_id):
    exam = Exam.find_by_exam_id(exam_id)
    exam.published = True
    db.session.commit()
    response = jsonify(
        status="success",
        message="successfully publish the exam",
    )
    response.status_code = HTTPStatus.OK
    response.headers["Cache-Control"] = "no-store"
    response.headers["Pragma"] = "no-cache"
    return response

@token_required
def process_upload_question_file_request(question_file):
    filename = secure_filename(question_file.filename)
    try:
        tmp_data = question_file.read().decode()
        data = yaml.load(tmp_data, SafeLoader)

        # Validate yaml format
        data_keys = [set(d.keys()) for d in data]
        for k in data_keys:
            if k != set(["question","choices","answer"]):
                return False

        result = validate_yaml(tmp_data)

        if not result:
            raise Exception("Invalid Yaml File")

        upload_path = os.path.join(current_app.config.get("UPLOAD_PATH"), filename)

        # Add instance creation signature for Question class and save the final yaml
        tmp_data = tmp_data.replace("  ","    ")
        tmp_data = tmp_data.replace("question:", "!!python/object:Question\n  kwds:\n    question:")
        with open(upload_path, "w") as f:
            f.write(tmp_data)

        response = jsonify(
            status="success",
            message="successfully uploaded",
            filename=filename
        )
        response.status_code = HTTPStatus.CREATED
        response.headers["Cache-Control"] = "no-store"
        response.headers["Pragma"] = "no-cache"
        return response

    except Exception as e:
        print(e)
        response = jsonify(
            status="fail",
            message="invalid yaml file",
        )
        response.status_code = HTTPStatus.BAD_REQUEST
        response.headers["Cache-Control"] = "no-store"
        response.headers["Pragma"] = "no-cache"
        return response

@teacher_token_required
def get_list_all_exam():
    user_id = get_list_all_exam.public_id
    exam = Exam.get_all(user_id)
    return exam

@token_required
def get_list_all_published_exam():
    exam = Exam.get_all_published()
    return exam

@token_required
def get_exam_by_id(exam_id):
    user_id = get_exam_by_id.public_id
    exam = Exam.find_by_exam_id(exam_id)
    question_file = os.path.join(current_app.config.get("UPLOAD_PATH"), exam.question_file)
    with open(question_file) as f:
        data = remove_duplicate(yaml.load(f, FullLoader))
    
    questions = []
    answer = {}
    for idx,obj_question in enumerate(data):
        tmp_question = obj_question.get_question_and_choices()
        tmp_question.update({"no":str(idx+1)})
        questions.append(tmp_question)
        answer[idx+1] = obj_question.get_answer()

    answer_filename = f"{user_id}_{exam_id}.answer"
    answer_filepath = os.path.join(current_app.config.get("EXAM_ANSWER_PATH"), answer_filename)
    with open(answer_filepath, "w") as f:
        f.write(json.dumps(answer))

    return jsonify(questions)

@token_required
def get_exam_result(exam_id, student_answer):
    user_id = get_exam_result.public_id    
    answer_filename = f"{user_id}_{exam_id}.answer"
    answer_filepath = os.path.join(current_app.config.get("EXAM_ANSWER_PATH"), answer_filename)
    with open(answer_filepath) as f:
        valid_answer = json.loads(f.read())

    valid_answer_from_student = 0
    for id in valid_answer.keys():
        if valid_answer[id] == student_answer.get(id):
            valid_answer_from_student += 1
    
    score = (valid_answer_from_student/len(valid_answer)) * 100
    response = jsonify(
        status="success",
        message=f"Your score is {score}"
    )
    return response
