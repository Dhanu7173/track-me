from ..models import *
from datetime import datetime

class Company(AppModel):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # FK to Users table
    company_name = db.Column(db.String(255), nullable=False)
    business_type = db.Column(db.String(100), nullable=False)
    industry = db.Column(db.String(100), nullable=False)
    company_reg_number = db.Column(db.String(50), unique=True, nullable=False)
    date_of_incorporation = db.Column(db.Date, nullable=False)
    website = db.Column(db.String(255), nullable=True)
    registered_address = db.Column(db.Text, nullable=False)
    state = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    gst_number = db.Column(db.String(50), unique=True, nullable=True)
    pan_number = db.Column(db.String(50), unique=True, nullable=True)
    gst_certificate_upload = db.Column(db.String(255), nullable=True)  # File path
    years_in_business = db.Column(db.Integer, nullable=False)
    current_clients = db.Column(db.Text, nullable=True)  # Storing as comma-separated values
    preferred_payment_terms = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    # user = db.relationship('Users', backref=db.backref('companies', lazy=True))
