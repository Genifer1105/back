from flask import Blueprint, jsonify, request
from app.modules.auth import AuthService
from werkzeug.exceptions import BadRequest
from app.utils import Utils

auth_blueprint = Blueprint('/auth', __name__)

@auth_blueprint.route('/create_user', methods=['POST'])
def create_user():
    user_data = request.json
    if not user_data:
        raise BadRequest()
    identificacion = Utils.validate_json_field(user_data, 'identificacion', int, True)
    nombre = Utils.validate_json_field(user_data, 'nombre', str, True)
    apellido1 = Utils.validate_json_field(user_data, 'apellido1', str, True)
    apellido2 = Utils.validate_json_field(user_data, 'apellido2', str, False)
    correo = Utils.validate_json_field(user_data, 'correo', str, True)
    contrasena = Utils.validate_json_field(user_data, 'contrasena', str, True)
    id_perfil = Utils.validate_json_field(user_data, 'id_perfil', int, True)
    telefono = Utils.validate_json_field(user_data, 'telefono', str, False)
    data = AuthService.create_user(identificacion, nombre, apellido1, apellido2, correo, contrasena, id_perfil, telefono)
    return jsonify({ "success": True, "data": data })

@auth_blueprint.route('/update_user/<identificacion>', methods=['PUT'])
def update_user(identificacion):
    user_data = request.json
    if not user_data:
        raise BadRequest()
    # identificacion = Utils.validate_field(identificacion, 'identificacion', int, True)
    nombre = Utils.validate_json_field(user_data, 'nombre', False, str)
    apellido1 = Utils.validate_json_field(user_data, 'apellido1', False, str)
    apellido2 = Utils.validate_json_field(user_data, 'apellido2', False, str)
    correo = Utils.validate_json_field(user_data, 'correo', False, str)
    id_perfil = Utils.validate_json_field(user_data, 'id_perfil', False, int)
    telefono = Utils.validate_json_field(user_data, 'telefono', False, str)
    data = AuthService.update_user(identificacion, nombre, apellido1, apellido2, correo, id_perfil, telefono)
    return jsonify({ "success": True, "data": data })

@auth_blueprint.route("/get_users", methods=['GET'])
def get_users():
    payload = AuthService.get_users()
    return jsonify(payload)

@auth_blueprint.route("/get_user/<identificacion>", methods=['GET'])
def get_user(identificacion):
    payload = AuthService.get_user(identificacion)
    return jsonify(payload)
    