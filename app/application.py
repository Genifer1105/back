from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.repositories import db_context    
from flask_cors import CORS
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
        return Application.app

    @staticmethod
    def register_routes(app: Flask):
        from app.modules.auth import auth_blueprint
        app.register_blueprint(auth_blueprint, url_prefix='/auth')
        from app.modules.animales import animal_blueprint
        app.register_blueprint(animal_blueprint, url_prefix='/animales')