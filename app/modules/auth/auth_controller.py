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
    identificacion = Utils.validate_json_field(user_data, 'identificacion', True, int)
    nombre = Utils.validate_json_field(user_data, 'nombre', True, str)
    apellido1 = Utils.validate_json_field(user_data, 'apellido1', True, str)
    apellido2 = Utils.validate_json_field(user_data, 'apellido2', False, str)
    correo = Utils.validate_json_field(user_data, 'correo', True, str)
    contrasena = Utils.validate_json_field(user_data, 'contrasena', True, str)
    id_perfil = Utils.validate_json_field(user_data, 'id_perfil', True, int)
    telefono = Utils.validate_json_field(user_data, 'telefono', False, str)
    data = AuthService.create_user(identificacion, nombre, apellido1, apellido2, correo, contrasena, id_perfil, telefono)
    return jsonify({ "success": True, "data": data })

@auth_blueprint.route('/login', methods=['POST'])
def login():
    login_data = request.json
    if not login_data:
        raise BadRequest()
    identificacion = Utils.validate_json_field(login_data, 'identificacion', True, int)
    contrasena = Utils.validate_json_field(login_data, 'contrasena', True, str)
    data = AuthService.login(identificacion, contrasena)
    return jsonify({"data": data, "success": True})
        

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
    