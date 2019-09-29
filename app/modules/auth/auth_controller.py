from flask import Blueprint, jsonify, request
from app.modules.auth import AuthService
from werkzeug.exceptions import BadRequest

auth_blueprint = Blueprint('/auth', __name__)

@auth_blueprint.route('/hola', methods=['GET'])
def hola():
    payload = { "message": "Holii =)" }
    return jsonify(payload)

@auth_blueprint.route('/create_user', methods=['POST'])
def create_user():
    user_data = request.json
    if not user_data:
        raise BadRequest()
    data = AuthService.create_user(user_data)
    return jsonify({ "success": True, "data": data })

@auth_blueprint.route('/update_user/<identificacion>', methods=['PUT'])
def update_user(identificacion):
    user_data = request.json
    try:
        identificacion = int(identificacion)
    except ValueError:
        raise BadRequest("identificacion must be an integer")
    data = AuthService.update_user(user_data, identificacion)
    return jsonify({ "success": True, "data": data })

@auth_blueprint.route("/get_users", methods=['GET'])
def get_users():
    payload = AuthService.get_users()
    return jsonify(payload)
    