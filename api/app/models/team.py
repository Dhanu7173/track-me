from ..models import db, AppModel
from datetime import datetime

class ProjectMembers(AppModel):
    __tablename__ = 'project_members'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role = db.Column(db.String(50), default="Member")  # Owner, Admin, Member
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user = db.relationship('Users', backref='project_members')
