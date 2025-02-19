import redis
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail
from flask_jwt_extended import JWTManager
from .config import Config

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
mail = Mail()
jwt = JWTManager()

# Initialize Redis
redis_client = redis.StrictRedis(
	host=Config.REDIS_HOST,
	port=Config.REDIS_PORT,
	db=Config.REDIS_DB,
	decode_responses=True  # Ensures we get strings instead of bytes
)
