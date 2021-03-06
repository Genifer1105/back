from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.repositories import db_context    
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

class Application:
    
    app: Flask = None

    @staticmethod
    def create_app():
        if not Application.app:
            Application.app = Flask(__name__)
            CORS(Application.app)
            Application.app.config.from_object('app.config.Configuration')
            db_context.init_app(Application.app)
            Application.register_routes(Application.app)
            Application.register_error_handlers(Application.app)
        return Application.app

    @staticmethod
    def register_error_handlers(app: Flask):
        app.register_error_handler(HTTPException, Application.error_handler)

    @staticmethod
    def register_routes(app: Flask):
        from app.modules.auth import auth_blueprint
        app.register_blueprint(auth_blueprint, url_prefix='/auth')
        from app.modules.animales import animal_blueprint
        app.register_blueprint(animal_blueprint, url_prefix='/animales')

    @staticmethod
    def error_handler(error):
        response = jsonify({ "message": error.description })
        response.status_code = error.code if isinstance(error, HTTPException) else 500
        return response