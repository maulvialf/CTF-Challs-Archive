"""Parsers and serializers for /auth API endpoints."""
from flask_restx.reqparse import RequestParser
import werkzeug
from flask_restx import Model
from flask_restx.fields import String, Integer, Boolean


exam_reqparser = RequestParser(bundle_errors=True)
exam_reqparser.add_argument(
    name="name", type=str, location="json", required=True, nullable=False
)
exam_reqparser.add_argument(
    name="time_limit", type=int, location="json", required=True, nullable=False
)
exam_reqparser.add_argument(
    name="question_file", type=str, location="json", required=True, nullable=False
)

file_reqparser = RequestParser(bundle_errors=True)
file_reqparser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')

answer_reqparser = RequestParser(bundle_errors=True)
answer_reqparser.add_argument(
    name="answers", type=dict, location="json",required=True, nullable=False
)

exam_model = Model(
    "Exam",
    {
        "exam_id": String,
        "exam_name": String,
        "time_limit": Integer,
        "published": Boolean
    },
)