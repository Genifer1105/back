from flask import Blueprint, jsonify, request
from app.modules.auth import AuthService

auth_blueprint = Blueprint('/auth', __name__)

@auth_blueprint.route('/hola', methods=['GET'])
def hola():
    payload = { "message": "Holii =)" }
    return jsonify(payload)

@auth_blueprint.route('/create_user', methods=['POST'])
def create_user():
    user_data = request.json
    AuthService.create_user(user_data)
    return jsonify({ "success": True })

@auth_blueprint.route('/update_user', methods=['PUT'])
def update_user():
    user_data = request.json
    AuthService.update_user(user_data)
    return jsonify({ "success": True })

@auth_blueprint.route("/get_users", methods=['GET'])
def get_users():
    payload = AuthService.get_users()
    return jsonify(payload)
    