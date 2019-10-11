from flask import Blueprint, jsonify, request
from app.modules.animales import AnimalService
from app.utils import Utils

animal_blueprint = Blueprint('/animales', __name__)

@animal_blueprint.route('/create_animal', methods=['POST'])
def create_animal():
    data = request.json
    identificacion_animal = Utils.validate_json_field(data.get, 'identificacion_animal', True, int)
    id_raza = Utils.validate_json_field(data.get, 'id_raza', True, int)
    fecha_nacimiento = Utils.validate_json_field(data.get, 'fecha_nacimiento', True, str)
    id_madre = Utils.validate_json_field(data.get, 'id_madre', False, int)
    id_padre = Utils.validate_json_field(data.get, 'id_padre', False, int)
    procedencia = Utils.validate_json_field(data.get, 'procedencia', True, int)
    fecha_nacimiento_date = Utils.convert_to_date(fecha_nacimiento, '%Y-%m-%d')
    jsonify(AnimalService.create_animal(identificacion_animal, id_raza, id_madre, id_padre, procedencia, fecha_nacimiento_date))
    return jsonify({ "success": True })

@animal_blueprint.route("/get_animals", methods=['GET'])
def get_users():
    payload = AnimalService.get_animals()
    return jsonify(payload)