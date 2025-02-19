from ..models import *

class BankDetails(AppModel):
    __tablename__ = 'bank_details'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # FK to Users table
    account_number = db.Column(db.String(20), unique=True, nullable=False)
    ifsc_code = db.Column(db.String(15), nullable=False)

    user = db.relationship('Users', backref=db.backref('bank_details', lazy=True))
