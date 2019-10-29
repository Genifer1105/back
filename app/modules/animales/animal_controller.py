from flask import Blueprint, jsonify, request
from app.modules.animales import AnimalService
from werkzeug.exceptions import BadRequest
from app.utils import Utils

animal_blueprint = Blueprint('/animales', __name__)

@animal_blueprint.route('/create_animal', methods=['POST'])
def create_animal():
    data = request.json
    if not data:
        raise BadRequest()
    identificacion_animal = Utils.validate_json_field(data, 'identificacion_animal', True, int)
    raza = Utils.validate_json_field(data, 'raza', True, str)
    fecha_nacimiento = Utils.validate_json_field(data, 'fecha_nacimiento', True, str)
    id_madre = Utils.validate_json_field(data, 'id_madre', False, int)
    id_padre = Utils.validate_json_field(data, 'id_padre', False, int)
    procedencia = Utils.validate_json_field(data, 'procedencia', True, str)
    fecha_nacimiento_date = Utils.convert_to_date(fecha_nacimiento, '%Y-%m-%d')
    result = AnimalService.create_animal(identificacion_animal, raza, id_madre, id_padre, procedencia, fecha_nacimiento_date)
    return jsonify({ "success": True, "data": result })

@animal_blueprint.route('/update_animal/<identificacion_animal>', methods=['PUT'])
def update_animal(identificacion_animal):
    data = request.json
    if not data:
        raise BadRequest()
    raza = Utils.validate_json_field(data, 'raza', True, str)
    fecha_nacimiento = Utils.validate_json_field(data, 'fecha_nacimiento', True, str)
    id_madre = Utils.validate_json_field(data, 'id_madre', False, int)
    id_padre = Utils.validate_json_field(data, 'id_padre', False, int)
    procedencia = Utils.validate_json_field(data, 'procedencia', True, str)
    fecha_nacimiento_date = Utils.convert_to_date(fecha_nacimiento, '%Y-%m-%d')
    result = AnimalService.update_animal(identificacion_animal, raza, id_madre, id_padre, procedencia, fecha_nacimiento_date)
    return jsonify({ "success": True, "data": result })

@animal_blueprint.route("/get_animals", methods=['GET'])
def get_animals():
    payload = AnimalService.get_animals()
    return jsonify(payload)

@animal_blueprint.route("/get_animal/<identificacion_animal>", methods=['GET'])
def get_animal(identificacion_animal):
    result = AnimalService.get_animal(identificacion_animal)
    return jsonify(result)

@animal_blueprint.route("/delete_animal/<identificacion_animal>", methods=['DELETE'])
def delete_animal(identificacion_animal):
    result = AnimalService.delete_animal(identificacion_animal)
    return jsonify({"success": True})