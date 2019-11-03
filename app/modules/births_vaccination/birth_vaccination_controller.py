from flask import Blueprint, jsonify, request
from app.modules.births_vaccination import BirthVaccinationService
from werkzeug.exceptions import BadRequest
from app.utils import Utils
from datetime import datetime

birth_vaccination_blueprint = Blueprint('/birth_vaccination', __name__)

@birth_vaccination_blueprint.route('/create_birth_vaccination', methods=['POST'])
def create_birth():
    data = request.json
    if not data:
        raise BadRequest()
    id_camada = Utils.validate_json_field(data, 'id_camada', True, int)
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
    result = BirthVaccinationService.create_birth_vaccination(
        id_camada, vacuna, fecha_programada_date, evento, fecha_ejecucion_date, 
        via_aplicacion, dosis, laboratorio, registro_ica, numero_lote, tiempo_retiro, 
        observaciones
    )
    return jsonify({ "success": True, "data": result })

@birth_vaccination_blueprint.route('/update_birth_vaccination/<id_camada>/<vacuna>/<fecha_programada>', methods=['PUT'])
def update_birth(id_camada, vacuna, fecha_programada):
    data = request.json
    if not data:
        raise BadRequest()
    id_camada = Utils.validate_field(id_camada, 'id_camada', str, True)
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
    result = BirthVaccinationService.update_birth_vaccination(
        id_camada, vacuna, fecha_programada_date, evento, fecha_ejecucion_date, 
        via_aplicacion, dosis, laboratorio, registro_ica, numero_lote, tiempo_retiro, 
        observaciones
    )
    return jsonify({ "success": True, "data": result })


@birth_vaccination_blueprint.route('/get_birth_vaccination_item/<id_camada>/<vacuna>/<fecha_programada>', methods=['GET'])
def get_birth_vaccination_item(id_camada, vacuna, fecha_programada):
    # id_camada = request.args.get('id_camada')
    # vacuna = request.args.get('vacuna')
    # fecha_programada = request.args.get('fecha_programada')
    id_camada = Utils.validate_field(id_camada, 'id_camada', str, True)
    vacuna = Utils.validate_field(vacuna, 'vacuna', str, True)
    fecha_programada = Utils.validate_field(fecha_programada, 'fecha_programada', str, True)
    fecha_programada_date = Utils.convert_to_date(fecha_programada, "%Y-%m-%d")
    result = BirthVaccinationService.get_birth_vaccination_item(id_camada, vacuna, fecha_programada_date)
    return jsonify(result)

@birth_vaccination_blueprint.route("/get_birth_vaccinations/<id_camada>", methods=['GET'])
def get_birth_vaccinations(id_camada):
    id_camada = Utils.validate_field(id_camada, 'id_camada', str, True)
    result = BirthVaccinationService.get_birth_vaccinations(id_camada)
    return jsonify(result)

@birth_vaccination_blueprint.route("/get_births_vaccinations", methods=['GET'])
def get_births():
    payload = BirthVaccinationService.get_births_vaccinations()
    return jsonify(payload)

# @birth_vaccination_blueprint.route("/get_birth/<id_camada>", methods=['GET'])
# def get_birth(id_camada):
#     result = AnimalService.get_birth(id_camada)
#     return jsonify(result)