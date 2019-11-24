from flask import Blueprint, jsonify, request
from app.modules.animals_vaccination import AnimalVaccinationService
from werkzeug.exceptions import BadRequest
from app.utils import Utils
from datetime import datetime
from app.decorators import authorize

animal_vaccination_blueprint = Blueprint('/animals_vaccination', __name__)

@animal_vaccination_blueprint.route('/create_animal_vaccination', methods=['POST'])
@authorize()
def create_animal():
    data = request.json
    if not data:
        raise BadRequest()
    identificacion_animal = Utils.validate_json_field(data, 'identificacion_animal', True, int)
    vacuna = Utils.validate_json_field(data, 'vacuna', True, str)
    fecha_programada = Utils.validate_json_field(data, 'fecha_programada', True, str)
    evento = Utils.validate_json_field(data, 'evento', True, str)
    fecha_ejecucion = Utils.validate_json_field(data, 'fecha_ejecucion', False, str)
    via_aplicacion = Utils.validate_json_field(data, 'via_aplicacion', True, str)
    dosis = Utils.validate_json_field(data, 'dosis', True, int)
    laboratorio = Utils.validate_json_field(data, 'laboratorio', True, str)
    registro_ica = Utils.validate_json_field(data, 'registro_ica', True, str)
    numero_lote = Utils.validate_json_field(data, 'numero_lote', True, str)
    tiempo_retiro = Utils.validate_json_field(data, 'tiempo_retiro', False, str)
    observaciones = Utils.validate_json_field(data, 'observaciones', False, str)
    fecha_programada_date = Utils.convert_to_date(fecha_programada, '%Y-%m-%d')
    
    fecha_ejecucion_date = Utils.convert_to_date(fecha_ejecucion, '%Y-%m-%d') if fecha_ejecucion else None
    result = AnimalVaccinationService.create_animal_vaccination(
        identificacion_animal, vacuna, fecha_programada_date, evento, fecha_ejecucion_date, 
        via_aplicacion, dosis, laboratorio, registro_ica, numero_lote, tiempo_retiro, 
        observaciones
    )
    return jsonify({ "success": True, "data": result })

@animal_vaccination_blueprint.route('/update_animal_vaccination/<identificacion_animal>/<vacuna>/<fecha_programada>', methods=['PUT'])
@authorize()
def update_animal(identificacion_animal, vacuna, fecha_programada):
    data = request.json
    if not data:
        raise BadRequest()
    identificacion_animal = Utils.validate_field(identificacion_animal, 'identificacion_animal', str, True)
    vacuna = Utils.validate_field(vacuna, 'vacuna', str, True)
    fecha_programada = Utils.validate_field(fecha_programada, 'fecha_programada', str, True)
    evento = Utils.validate_json_field(data, 'evento', True, str)
    fecha_ejecucion = Utils.validate_json_field(data, 'fecha_ejecucion', False, str)
    via_aplicacion = Utils.validate_json_field(data, 'via_aplicacion', True, str)
    dosis = Utils.validate_json_field(data, 'dosis', True, int)
    laboratorio = Utils.validate_json_field(data, 'laboratorio', True, str)
    registro_ica = Utils.validate_json_field(data, 'registro_ica', True, str)
    numero_lote = Utils.validate_json_field(data, 'numero_lote', True, str)
    tiempo_retiro = Utils.validate_json_field(data, 'tiempo_retiro', False, str)
    observaciones = Utils.validate_json_field(data, 'observaciones', False, str)
    fecha_programada_date = Utils.convert_to_date(fecha_programada, '%Y-%m-%d')
    
    fecha_ejecucion_date = Utils.convert_to_date(fecha_ejecucion, '%Y-%m-%d') if fecha_ejecucion else None
    result = AnimalVaccinationService.update_animal_vaccination(
        identificacion_animal, vacuna, fecha_programada_date, evento, fecha_ejecucion_date, 
        via_aplicacion, dosis, laboratorio, registro_ica, numero_lote, tiempo_retiro, 
        observaciones
    )
    return jsonify({ "success": True, "data": result })


@animal_vaccination_blueprint.route('/get_animal_vaccination_item/<identificacion_animal>/<vacuna>/<fecha_programada>', methods=['GET'])
@authorize()
def get_animal_vaccination_item(identificacion_animal, vacuna, fecha_programada):
    # identificacion_animal = request.args.get('identificacion_animal')
    # vacuna = request.args.get('vacuna')
    # fecha_programada = request.args.get('fecha_programada')
    identificacion_animal = Utils.validate_field(identificacion_animal, 'identificacion_animal', str, True)
    vacuna = Utils.validate_field(vacuna, 'vacuna', str, True)
    fecha_programada = Utils.validate_field(fecha_programada, 'fecha_programada', str, True)
    fecha_programada_date = Utils.convert_to_date(fecha_programada, "%Y-%m-%d")
    result = AnimalVaccinationService.get_animal_vaccination_item(identificacion_animal, vacuna, fecha_programada_date)
    return jsonify(result)

@animal_vaccination_blueprint.route("/get_animal_vaccinations/<identificacion_animal>", methods=['GET'])
@authorize()
def get_animal_vaccinations(identificacion_animal):
    identificacion_animal = Utils.validate_field(identificacion_animal, 'identificacion_animal', str, True)
    result = AnimalVaccinationService.get_animal_vaccinations(identificacion_animal)
    return jsonify(result)

@animal_vaccination_blueprint.route("/get_animals_vaccinations", methods=['GET'])
@authorize()
def get_animals():
    payload = AnimalVaccinationService.get_animals_vaccinations()
    return jsonify(payload)

# @animal_vaccination_blueprint.route("/get_animal/<identificacion_animal>", methods=['GET'])
# def get_animal(identificacion_animal):
#     result = AnimalService.get_animal(identificacion_animal)
#     return jsonify(result)