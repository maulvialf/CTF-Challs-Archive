from http import HTTPStatus
from flask_restx import Namespace, Resource
from .dto import exam_reqparser, file_reqparser, answer_reqparser, exam_model
from .business import (
    delete_exam,
    get_exam_by_id,
    get_exam_result,
    get_list_all_exam,
    get_list_all_published_exam,
    process_exam_creation_request,
    process_upload_question_file_request,
    publish_exam,
)

exam_ns = Namespace(name="exam", validate=True)


@exam_ns.route("/create", endpoint="create_exam")
class CreateExam(Resource):
    """Handles HTTP requests to URL: /api/v1/exam/create."""

    @exam_ns.expect(exam_reqparser)
    @exam_ns.response(int(HTTPStatus.CREATED), "A new exam was successfully created.")
    @exam_ns.response(int(HTTPStatus.CONFLICT), "Exam with the same name is already exist.")
    @exam_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @exam_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def post(self):
        request_data = exam_reqparser.parse_args()
        name = request_data.get("name")
        limit = request_data.get("time_limit")
        question_file = request_data.get("question_file")
        return process_exam_creation_request(name, limit, question_file)

@exam_ns.route("/upload", endpoint="upload_question")
class UploadQuestion(Resource):
    """Handles HTTP requests to URL: /api/v1/exam/upload."""

    @exam_ns.doc(security="Bearer")
    @exam_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @exam_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def post(self):
        question_file = file_reqparser.parse_args()
        return process_upload_question_file_request(question_file['file'])

@exam_ns.route("/all", endpoint="list_exam")
class GetAllExam(Resource):
    """Handles HTTP requests to URL: /api/v1/exam/all."""

    @exam_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @exam_ns.response(int(HTTPStatus.UNAUTHORIZED), "Token is invalid or expired.")
    @exam_ns.marshal_with(exam_model)
    def get(self):
        return get_list_all_exam()

@exam_ns.route("/published", endpoint="list_published_exam")
class GetPublishedExam(Resource):
    """Handles HTTP requests to URL: /api/v1/exam/published."""

    @exam_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @exam_ns.response(int(HTTPStatus.UNAUTHORIZED), "Token is invalid or expired.")
    @exam_ns.marshal_with(exam_model)
    def get(self):
        return get_list_all_published_exam()

@exam_ns.route("/<string:exam_id>/start", endpoint="start_exam")
class GetExamById(Resource):
    """Handles HTTP requests to URL: /api/v1/exam/<uuid>/start."""

    @exam_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @exam_ns.response(int(HTTPStatus.UNAUTHORIZED), "Token is invalid or expired.")
    def get(self, exam_id):
        return get_exam_by_id(exam_id)

@exam_ns.route("/<string:exam_id>", endpoint="delete_exam")
class DeleteExam(Resource):
    @exam_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @exam_ns.response(int(HTTPStatus.UNAUTHORIZED), "Token is invalid or expired.")
    def delete(self, exam_id):
        return delete_exam(exam_id)

@exam_ns.route("/<string:exam_id>", endpoint="publish_exam")
class PublishExam(Resource):
    @exam_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @exam_ns.response(int(HTTPStatus.UNAUTHORIZED), "Token is invalid or expired.")
    def put(self, exam_id):
        return publish_exam(exam_id)


@exam_ns.route("/<string:exam_id>/submit", endpoint="end_exam")
class GetExamResult(Resource):
    """Handles HTTP requests to URL: /api/v1/exam/<uuid>/submit."""

    @exam_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @exam_ns.response(int(HTTPStatus.UNAUTHORIZED), "Token is invalid or expired.")
    def post(self, exam_id):
        answer = answer_reqparser.parse_args()
        return get_exam_result(exam_id, answer.get('answers', {}))