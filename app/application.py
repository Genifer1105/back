from flask import Flask
from app.modules.auth import auth_blueprint

class Application:

    @staticmethod
    def create_app():
        app = Flask(__name__)
        Application.register_routes(app)
        return app

    @staticmethod
    def register_routes(app: Flask):
        app.register_blueprint(auth_blueprint, url_prefix='/auth')