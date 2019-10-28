from flask import Blueprint, jsonify, request
from app.modules.animals_vaccination import AnimalVaccinationService
from werkzeug.exceptions import BadRequest
from app.utils import Utils
from datetime import datetime

animal_vaccination_blueprint = Blueprint('/animals_vaccination', __name__)

@animal_vaccination_blueprint.route('/create_animal', methods=['POST'])
def create_animal():
    data = request.json
    if not data:
        raise BadRequest()
    identificacion_animal = Utils.validate_json_field(data, 'identificacion_animal', True, int)
    vacuna = Utils.validate_json_field(data, 'vacuna', True, str)
    fecha_programada = Utils.validate_json_field(data, 'fecha_programada', True, datetime)
    evento = Utils.validate_json_field(data, 'evento', True, str)
    fecha_ejecucion = Utils.validate_json_field(data, 'fecha_ejecucion', False, datetime)
    via_aplicacion = Utils.validate_json_field(data, 'via_aplicacion', True, str)
    dosis = Utils.validate_json_field(data, 'dosis', True, int)
    laboratorio = Utils.validate_json_field(data, 'laboratorio', True, str)
    reg_ica = Utils.validate_json_field(data, 'reg_ica', True, str)
    nro_lote = Utils.validate_json_field(data, 'nro_lote', True, str)
    tiempo_retiro = Utils.validate_json_field(data, 'tiempo_retiro', False, str)
    observaciones = Utils.validate_json_field(data, 'observaciones', False, str)
    result = AnimalService.create_animal(identificacion_animal, raza, id_madre, id_padre, procedencia, fecha_nacimiento_date)
    return jsonify({ "success": True, "data": result })

@animal_vaccination_blueprint.route('/update_animal/<identificacion_animal>', methods=['PUT'])
def update_animal(identificacion_animal):
    data = request.json
    if not data:
        raise BadRequest()
    raza = Utils.validate_json_field(data, 'raza', True, int)
    fecha_nacimiento = Utils.validate_json_field(data, 'fecha_nacimiento', True, str)
    id_madre = Utils.validate_json_field(data, 'id_madre', False, int)
    id_padre = Utils.validate_json_field(data, 'id_padre', False, int)
    procedencia = Utils.validate_json_field(data, 'procedencia', True, int)
    fecha_nacimiento_date = Utils.convert_to_date(fecha_nacimiento, '%Y-%m-%d')
    result = AnimalService.update_animal(identificacion_animal, raza, id_madre, id_padre, procedencia, fecha_nacimiento_date)
    return jsonify({ "success": True, "data": result })

@animal_vaccination_blueprint.route("/get_animals", methods=['GET'])
def get_animals():
    payload = AnimalService.get_animals()
    return jsonify(payload)

@animal_vaccination_blueprint.route("/get_animal/<identificacion_animal>", methods=['GET'])
def get_animal(identificacion_animal):
    result = AnimalService.get_animal(identificacion_animal)
    return jsonify(result)