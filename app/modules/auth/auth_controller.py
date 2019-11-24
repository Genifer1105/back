from flask import Blueprint, jsonify, request
from app.modules.auth import AuthService
from werkzeug.exceptions import BadRequest
from app.utils import Utils
from app.decorators import authorize
from flask_jwt_extended import get_jwt_identity

auth_blueprint = Blueprint('/auth', __name__)

# @auth_blueprint.route('/admin_required')
# @authorize()
# def admin_required():
#     return jsonify({ "success": True })

# @auth_blueprint.route('/not_admin_required')
# @authorize()
# def not_admin_required():
#     return jsonify({ "success": True })

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
    if len(contrasena) < 8:
        raise BadRequest('password min length is 8 chars')
    data = AuthService.create_user(identificacion, nombre, apellido1, apellido2, correo, contrasena, id_perfil, telefono)
    return jsonify({ "success": True, "data": data })

@auth_blueprint.route('/login', methods=['POST'])
def login():
    login_data = request.json
    if not login_data:
        raise BadRequest()
    identificacion = Utils.validate_json_field(login_data, 'identificacion', False, int)
    contrasena = Utils.validate_json_field(login_data, 'contrasena', True, str)
    correo = Utils.validate_json_field(login_data, 'correo', identificacion is None, str)
    data, token = AuthService.login(identificacion, correo, contrasena)
    return jsonify({"data": data, "success": True, "token": token})
        

@auth_blueprint.route('/update_user/<identificacion>', methods=['PUT'])
@authorize(1)
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
@authorize(1)
def get_users():
    payload = AuthService.get_users()
    return jsonify(payload)

@auth_blueprint.route("/get_user/<identificacion>", methods=['GET'])
@authorize(1)
def get_user(identificacion):
    payload = AuthService.get_user(identificacion)
    return jsonify(payload)

@auth_blueprint.route("/get_logged_user", methods=['GET'])
@authorize()
def get_logged_user():
    data = get_jwt_identity()
    identificacion = data.get('identificacion')    
    payload = AuthService.get_user(identificacion)
    return jsonify(payload)

@auth_blueprint.route("/send_recovery_mail", methods=['POST'])
def get_send_mail():
    request_data = request.json
    if not request_data:
        raise BadRequest()
    email_to_send = Utils.validate_json_field(request_data, 'email', True, str)
    AuthService.password_recover(email_to_send)
    return jsonify({ "success": True })

@auth_blueprint.route("/change_password", methods=['POST'])
@authorize()
def change_password():
    request_data = request.json
    token_data = get_jwt_identity()
    if not request_data:
        raise BadRequest()
    identificacion = token_data.get('identificacion')    
    password = Utils.validate_json_field(request_data, 'password', True, str)
    new_password = Utils.validate_json_field(request_data, 'new_password', True, str)
    if len(new_password) < 8:
        raise BadRequest('password min length is 8 chars')
    AuthService.change_password(identificacion, password, new_password)
    return jsonify({ "success": True })
    