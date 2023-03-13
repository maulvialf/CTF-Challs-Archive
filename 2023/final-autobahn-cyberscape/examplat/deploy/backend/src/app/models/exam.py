"""Class definition for Exam model."""
from uuid import uuid4

from app import db

class Exam(db.Model):
    """Exam model."""

    __tablename__ = "exam_data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exam_name = db.Column(db.String(255), unique=True, nullable=False)
    time_limit = db.Column(db.Integer, nullable=False)
    question_file = db.Column(db.String(255), nullable=False)
    created_by = db.Column(db.String(36), nullable=False)
    published = db.Column(db.Boolean, nullable=False, default=False)
    exam_id = db.Column(db.String(36), unique=True, default=lambda: str(uuid4()))

    @classmethod
    def get_all(cls, user_id):
        return cls.query.filter_by(created_by=user_id).all()
    
    @classmethod
    def get_all_published(cls):
        return cls.query.filter_by(published=True).all()
        
    @classmethod
    def find_by_exam_id(cls, exam_id):
        return cls.query.filter_by(exam_id=exam_id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(exam_name=name).first()
    
    @classmethod
    def delete_if_exist(cls, exam_id, user_id):
        return cls.query.filter_by(exam_id=exam_id, created_by=user_id).delete()
    