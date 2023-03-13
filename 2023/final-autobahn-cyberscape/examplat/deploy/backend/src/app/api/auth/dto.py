"""Parsers and serializers for /auth API endpoints."""
from flask_restx import Model
from flask_restx.fields import String
from flask_restx.inputs import email
from flask_restx.reqparse import RequestParser


auth_reqparser = RequestParser(bundle_errors=True)
auth_reqparser.add_argument(
    name="email", type=email(), location="json", required=True, nullable=False
)
auth_reqparser.add_argument(
    name="password", type=str, location="json", required=True, nullable=False
)
auth_reqparser.add_argument(
    name="firstname", type=str, location="json", required=False, nullable=False
)
auth_reqparser.add_argument(
    name="lastname", type=str, location="json", required=False, nullable=False
)
auth_reqparser.add_argument(
    name="role", type=str, location="json", required=False, nullable=False
)

user_model = Model(
    "User",
    {
        "email": String,
        "firstname": String,
        "lastname": String,
        "public_id": String,
        "role": String,
        "registered_on": String(attribute="registered_on_str"),
        "token_expires_in": String,
        "photo": String
    },
)