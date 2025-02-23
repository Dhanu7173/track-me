from ..models import *
from datetime import datetime

class Users(AppModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Increased to 255 chars
    is_email_verified = db.Column(db.Boolean, default=False)
    is_phone_verified = db.Column(db.Boolean, default=False)
    kyc_status = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    category = db.Column(db.String(50), nullable=True)
    current_stage = db.Column(db.String(50), nullable=True)
    role = db.Column(db.String(50), nullable=True)
    extra_details = db.Column(db.JSON, nullable=True)

    # Relationships
    projects = db.relationship('Projects', backref='owner', lazy=True)
    tasks = db.relationship('Tasks', backref='assignee', lazy=True)