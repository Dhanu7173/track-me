from flask import Flask
from .config import Config
from .extensions import db, migrate, cors, mail, jwt


def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	migrate.init_app(app, db)
	cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
	mail.init_app(app)
	jwt.init_app(app)
	from .views import register_blueprints
	register_blueprints(app)

	return app
