from flask import Flask, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from app.repositories import db_context    
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from werkzeug.exceptions import HTTPException

class Application:
    
    app: Flask = None

    @staticmethod
    def create_app():
        if not Application.app:
            Application.app = Flask(__name__, template_folder='templates')
            CORS(Application.app)
            JWTManager(Application.app)
            Application.app.config.from_object('app.config.Configuration')
            Application.app.jinja_env.globals['static'] = Application.static_file
            db_context.init_app(Application.app)
            Application.register_routes(Application.app)
            Application.register_error_handlers(Application.app)
        return Application.app

    @staticmethod
    def static_file(filename, pdf=False, root=None):
        path = None
        if(pdf):
            path = "".join([root, "static/", filename])
        else:
            path = url_for('static', filename=filename)
        print('path: ', path)
        return path

    @staticmethod
    def register_error_handlers(app: Flask):
        app.register_error_handler(HTTPException, Application.error_handler)

    @staticmethod
    def register_routes(app: Flask):
        from app.modules.auth import auth_blueprint
        app.register_blueprint(auth_blueprint, url_prefix='/auth')
        from app.modules.animales import animal_blueprint
        app.register_blueprint(animal_blueprint, url_prefix='/animales')
        # from app.modules.vaccines import vaccines_blueprint
        # app.register_blueprint(vaccines_blueprint, url_prefix='/vaccines')
        from app.modules.animals_vaccination import animal_vaccination_blueprint
        app.register_blueprint(animal_vaccination_blueprint, url_prefix='/animals_vaccination')
        from app.modules.births import birth_blueprint
        app.register_blueprint(birth_blueprint, url_prefix='/births')
        from app.modules.reports.reports_controller import reports_bluerpint
        app.register_blueprint(reports_bluerpint, url_prefix='/reports')
        from app.modules.births_vaccination import birth_vaccination_blueprint
        app.register_blueprint(birth_vaccination_blueprint, url_prefix='/births_vaccination')

    @staticmethod
    def error_handler(error):
        response = jsonify({ "message": error.description })
        response.status_code = error.code if isinstance(error, HTTPException) else 500
        return response