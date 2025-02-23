from ..models import db, AppModel
from datetime import datetime

class Projects(AppModel):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    type = db.Column(db.String(50), nullable=True)  # e.g., Software, Marketing, Construction
    progress = db.Column(db.Integer, default=0)  # Progress percentage
    status = db.Column(db.String(50), default="Pending")  # Pending, In Progress, Completed
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    due_date = db.Column(db.Date, nullable=True)
    
    # Remove JSON fields and establish relationships instead
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    updated_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationships
    team_members = db.relationship('ProjectMembers', backref='project', lazy=True)
    tasks = db.relationship('Tasks', backref='project', lazy=True)
    attachments = db.relationship('FileAttachments', backref='project', lazy=True)
    comments = db.relationship('ProjectComments', backref='project', lazy=True)

