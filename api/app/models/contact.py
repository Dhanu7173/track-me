from ..models import *

class ContactDetails(AppModel):
    __tablename__ = 'contact_details'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # FK to Users table
    full_name = db.Column(db.String(255), nullable=False)
    designation = db.Column(db.String(100), nullable=False)
    alternate_contact_number = db.Column(db.String(15), nullable=True)
    adhar_card = db.Column(db.String(20), unique=True, nullable=True)
    
    user = db.relationship('Users', backref=db.backref('contact_details', lazy=True))
