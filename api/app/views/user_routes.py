from datetime import datetime
import random

import requests
import yaml
from flask import Blueprint, request, jsonify, session
from ..models.user import Users
from ..models.projects import Projects
from ..extensions import db, mail, redis_client
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from flask_mail import Message
from twilio.rest import Client
from datetime import datetime

from sqlalchemy import desc

from ..config import Config
import json
from ..utils.auth import store_session

user_bp = Blueprint('user_bp', __name__)


@user_bp.route("/get_user_data", methods=["GET"])
def get_admin_user():
	if 'user' in session:
		user = Users.query.filter_by(email=session['user']['email']).first()
		user_data = {
            "token": session['token'],
			"is_logged_in": True,
			"user": {
				"id": user.id,
				"username": user.username,
				"email": user.email,
				"phone": user.phone,
				"stage": user.current_stage,
                "kyc_status": user.kyc_status
			}
		}
		return jsonify(ok=True, user_data=user_data)
	return jsonify(ok=False, error="user session expired")


@user_bp.route("/logout", methods=["GET"])
def logout():
	session.clear()
	return jsonify(ok=True, error="User has been successfully logged out")


@user_bp.route('/session', methods=['GET'])
def get_session():
	if 'user' not in session:
		return jsonify(ok=False, data={"msg": "No active session"})

	return jsonify(ok=True, data={
		"user": session.get('user'),
		"token": session.get('token'),
	})


def generate_otp():
	otp = str(random.randint(100000, 999999))
	print("Generating OTP", otp)
	return otp


def send_email_otp(email, otp):
	msg = Message("Your OTP Code", sender=Config.MAIL_USERNAME, recipients=[email])
	msg.body = f"Your OTP code is: {otp}. It will expire in 5 minutes."
	# mail.send(msg)


def send_sms_otp(phone, otp):
	client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)
	# client.messages.create(
	#     body=f"Your OTP code is: {otp}. It will expire in 5 minutes.",
	#     from_=Config.TWILIO_PHONE_NUMBER,
	#     to=phone
	# )


@user_bp.route('/send-email-otp', methods=['POST'])
def send_email_otp_route():
    data = request.json

    if not data or 'email' not in data:
        return jsonify({"error": "Email is required"}), 400

    email = data['email']

    if not email:
        return jsonify({"error": "Please fill in the Email"}), 400

    email_otp = generate_otp()
    redis_client.setex(f"otp_email_{email}", 300, email_otp)  # Expire in 5 min
    send_email_otp(email, email_otp)
    return jsonify(ok=True,message="Email OTP sent successfully")


@user_bp.route('/verify-email-otp', methods=['POST'])
def verify_email_otp():
	data = request.json
	stored_otp = redis_client.get(f"otp_email_{data['email']}")
	# stored_otp = "111111"
	if stored_otp and stored_otp == data['otp']:
		redis_client.delete(f"otp_email_{data['email']}")
		return jsonify(ok=True, message="OTP verified successfully.")
	else:
		return jsonify(ok=False, error="Invalid OTP.")


@user_bp.route('/send-phone-otp', methods=['POST'])
def send_phone_otp_route():
    data = request.json

    if not data or 'phone' not in data:
        return jsonify({"error": "Phone number is required"}), 400

    phone = data['phone']
    if not phone:
        return jsonify({"error": "Phone number cannot be empty"}), 400

    phone_otp = generate_otp()
    redis_client.setex(f"otp_phone_{phone}", 300, phone_otp)
    send_sms_otp(phone, phone_otp)
    return jsonify(ok=True,message="Phone OTP sent successfully")


@user_bp.route('/verify-phone-otp', methods=['POST'])
def verify_phone_otp():
	data = request.json
	stored_otp = redis_client.get(f"otp_phone_{data['phone']}")
	# stored_otp = "111111"
	if stored_otp and stored_otp == data['otp']:
		redis_client.delete(f"otp_phone_{data['phone']}")
		return jsonify(ok=True, message="OTP verified successfully.")
	else:
		return jsonify(ok=False, error="Invalid OTP.")


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Check if user exists
    user = Users.query.filter_by(email=email).first()
    if not user:
        return jsonify(ok=False, message="User not found")

    # Verify password
    if not check_password_hash(user.password, password):
        return jsonify(ok=False, message="Invalid password")

    # Update last_login
    user.last_login = datetime.utcnow()
    db.session.commit()

    # Generate JWT Token
    access_token = create_access_token(identity=user.id)

    user_data = {
        "token": access_token,
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "phone": user.phone,
            "stage": user.current_stage,
            "kyc_status": user.kyc_status
        }
    }
    store_session(user_data)

    return jsonify(ok=True, message="Login successful", data=user_data)


# ✅ REGISTER API (Updated Response Format)
@user_bp.route('/register', methods=['POST'])
def register_user():
	data = request.json

	# Ensure email and phone are verified before registration
	if not data.get('emailVerified') or not data.get('phoneVerified'):
		return jsonify(ok=False, message="Email and phone must be verified first")

	hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')

	# Create new user
	new_user = Users(
		username=data['username'],
		email=data['email'],
		phone=data['phone'],
		password=hashed_password,
		is_email_verified=True,
		is_phone_verified=True,
        kyc_status="Pending",
        role="dealer",
        current_stage="businessDetails",
		created_at=datetime.utcnow(),
		last_login=datetime.utcnow(),
		updated_at=datetime.utcnow()
	)

	db.session.add(new_user)
	db.session.commit()

	return jsonify(ok=True, message="User registered successfully!", data={
		"user": {
			"id": new_user.id,
			"username": new_user.username,
			"email": new_user.email,
            "phone": new_user.phone,
            "stage": new_user.current_stage,
            "kyc_status": new_user.kyc_status
		}
	})


def load_yaml(file_path='workflow.yaml'):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

@user_bp.route('/categories', methods=['GET'])
def get_categories():
    """Return list of categories"""
    data = load_yaml()
    
    categories = [category['name'] for category in data.get('categories', [])]
    return jsonify(categories)

@user_bp.route('/custom-fields/<category>', methods=['GET'])
def get_custom_fields_by_category(category):
    """Return custom fields for a specific category"""
    data = load_yaml()
    categories = data.get('categories', [])

    selected_category = next((c for c in categories if c['name'].lower() == category.lower()), None)

    if not selected_category:
        return jsonify({'error': 'Category not found'})

    return jsonify(selected_category['fields'])



# ################# Projects APIS ####################

@user_bp.route('/projects', methods=['POST'])
def create_project():
    try:
        data = request.json

        new_project = Projects(
            title=data['title'],
            description=data['description'],
            type=data['type'],
            progress=data['progress'],
            status=data['status'],
            start_date=data['startDate'],
            end_date=data['endDate'],
            due_date=data['dueDate'],
            team=data.get('team', []),  # Store team as JSON
            tasks=data.get('tasks', [])  # Store tasks as JSON
        )

        db.session.add(new_project)
        db.session.commit()

        return jsonify({"message": "Project added successfully", "project_id": new_project.id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
