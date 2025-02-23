from ..models import *
from datetime import datetime

class Tasks(AppModel):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), default="To Do")  # To Do, In Progress, Done
    priority = db.Column(db.String(50), default="Medium")  # Low, Medium, High
    assignee_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deadline = db.Column(db.DateTime, nullable=True)

    # Relationships
    assignee = db.relationship('Users', backref='tasks')
    comments = db.relationship('TaskComments', backref='task', lazy=True)
