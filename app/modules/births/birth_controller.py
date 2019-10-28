from flask import Blueprint, jsonify, request
from app.modules.births import BirthService
from werkzeug.exceptions import BadRequest
from app.utils import Utils

birth_blueprint = Blueprint('/births', __name__)

@birth_blueprint.route('/create_birth', methods=['POST'])
def create_birth():
    data = request.json
    if not data:
        raise BadRequest()
    id_camada = Utils.validate_json_field(data, 'id_camada', True, int)
    identificacion_animal  = Utils.validate_json_field(data, 'identificacion_animal', True, int) 
    fecha_monta = Utils.validate_json_field(data, 'fecha_monta', True, str)
    tipo_servicio = Utils.validate_json_field(data, 'tipo_servicio', True,  str)
    identificacion_macho = Utils.validate_json_field(data, 'identificacion_macho', False, int)
    fecha_probable_parto = Utils.validate_json_field(data, 'fecha_probable_parto', True, str)
    fecha_parto = Utils.validate_json_field(data, 'fecha_parto', True, str)
    jaula_parto = Utils.validate_json_field(data, 'jaula_parto', True, str)
    numero_lechones_vivos_parto = Utils.validate_json_field(data, 'numero_lechones_vivos_parto', True, int)
    numero_lechones_muertos_parto = Utils.validate_json_field(data, 'numero_lechones_muertos_parto', True, int)
    numero_machos_parto = Utils.validate_json_field(data, 'numero_machos_parto', True, int)
    numero_hembras_parto = Utils.validate_json_field(data, 'numero_hembras_parto', True, int)
    numero_momias = Utils.validate_json_field(data, 'numero_momias', True, int)
    peso_total_vivos = Utils.validate_json_field(data, 'peso_total_vivos', True,  int)
    fecha_probable_destete = Utils.validate_json_field(data, 'fecha_probable_destete', False, str)
    fecha_destete = Utils.validate_json_field(data, 'fecha_destete', False, str)
    numero_hembras_destete = Utils.validate_json_field(data, 'numero_hembras_destete', False, int)
    numero_machos_destete = Utils.validate_json_field(data, 'numero_machos_destete', False, int)
    numero_muertos_destete = Utils.validate_json_field(data, 'numero_muertos_destete', False, int)
    dias_lactancia = Utils.validate_json_field(data, 'dias_lactancia', True,  int)
    peso_total_destete = Utils.validate_json_field(data, 'peso_total_destete', True, int)
    jaula_destete = Utils.validate_json_field(data, 'jaula_destete', True, str)
    fecha_monta_date = Utils.convert_to_date(fecha_monta, "%Y-%m-%d") if fecha_monta is not None else None
    fecha_probable_parto_date = Utils.convert_to_date(fecha_probable_parto, "%Y-%m-%d") if fecha_probable_parto is not None else None
    fecha_parto_date = Utils.convert_to_date(fecha_parto, "%Y-%m-%d") if fecha_parto is not None else None
    fecha_probable_destete_date = Utils.convert_to_date(fecha_probable_destete, "%Y-%m-%d") if fecha_probable_destete is not None else None
    fecha_destete_date = Utils.convert_to_date(fecha_destete, "%Y-%m-%d")  if fecha_destete is not None else None
    result = BirthService.create_birth(
        id_camada, identificacion_animal, fecha_monta_date, tipo_servicio, 
        identificacion_macho, fecha_probable_parto_date, fecha_parto_date, jaula_parto, 
        numero_lechones_vivos_parto, numero_lechones_muertos_parto, 
        numero_machos_parto, numero_hembras_parto, numero_momias, peso_total_vivos, 
        fecha_probable_destete_date, fecha_destete_date, numero_hembras_destete, 
        numero_machos_destete, numero_muertos_destete, dias_lactancia, 
        peso_total_destete, jaula_destete
    )
    return jsonify({ "success": True, "data": result })

@birth_blueprint.route('/update_birth/<id_camada>', methods=['PUT'])
def update_birth(id_camada):
    data = request.json
    if not data:
        raise BadRequest()
    # id_camada = Utils.validate_field(data, 'id_camada', int, True)
    identificacion_animal  = Utils.validate_json_field(data, 'identificacion_animal', True, int) 
    fecha_monta = Utils.validate_json_field(data, 'fecha_monta', True, str)
    tipo_servicio = Utils.validate_json_field(data, 'tipo_servicio', True,  str)
    identificacion_macho = Utils.validate_json_field(data, 'identificacion_macho', False, int)
    fecha_probable_parto = Utils.validate_json_field(data, 'fecha_probable_parto', True, str)
    fecha_parto = Utils.validate_json_field(data, 'fecha_parto', True, str)
    jaula_parto = Utils.validate_json_field(data, 'jaula_parto', True, str)
    numero_lechones_vivos_parto = Utils.validate_json_field(data, 'numero_lechones_vivos_parto', True, int)
    numero_lechones_muertos_parto = Utils.validate_json_field(data, 'numero_lechones_muertos_parto', True, int)
    numero_machos_parto = Utils.validate_json_field(data, 'numero_machos_parto', True, int)
    numero_hembras_parto = Utils.validate_json_field(data, 'numero_hembras_parto', True, int)
    numero_momias = Utils.validate_json_field(data, 'numero_momias', True, int)
    peso_total_vivos = Utils.validate_json_field(data, 'peso_total_vivos', True,  int)
    fecha_probable_destete = Utils.validate_json_field(data, 'fecha_probable_destete', False, str)
    fecha_destete = Utils.validate_json_field(data, 'fecha_destete', False, str)
    numero_hembras_destete = Utils.validate_json_field(data, 'numero_hembras_destete', False, int)
    numero_machos_destete = Utils.validate_json_field(data, 'numero_machos_destete', False, int)
    numero_muertos_destete = Utils.validate_json_field(data, 'numero_muertos_destete', False, int)
    dias_lactancia = Utils.validate_json_field(data, 'dias_lactancia', True,  int)
    peso_total_destete = Utils.validate_json_field(data, 'peso_total_destete', True, int)
    jaula_destete = Utils.validate_json_field(data, 'jaula_destete', True, str)
    fecha_monta_date = Utils.convert_to_date(fecha_monta, "%Y-%m-%d") if fecha_monta is not None else None
    fecha_probable_parto_date = Utils.convert_to_date(fecha_probable_parto, "%Y-%m-%d") if fecha_probable_parto is not None else None
    fecha_parto_date = Utils.convert_to_date(fecha_parto, "%Y-%m-%d") if fecha_parto is not None else None
    fecha_probable_destete_date = Utils.convert_to_date(fecha_probable_destete, "%Y-%m-%d") if fecha_probable_destete is not None else None
    fecha_destete_date = Utils.convert_to_date(fecha_destete, "%Y-%m-%d")  if fecha_destete is not None else None
    result = BirthService.update_birth(
        id_camada, identificacion_animal, fecha_monta_date, tipo_servicio, 
        identificacion_macho, fecha_probable_parto_date, fecha_parto_date, jaula_parto, 
        numero_lechones_vivos_parto, numero_lechones_muertos_parto, 
        numero_machos_parto, numero_hembras_parto, numero_momias, peso_total_vivos, 
        fecha_probable_destete_date, fecha_destete_date, numero_hembras_destete, 
        numero_machos_destete, numero_muertos_destete, dias_lactancia, 
        peso_total_destete, jaula_destete
    )
    return jsonify({ "success": True, "data": result })

@birth_blueprint.route("/get_births", methods=['GET'])
def get_births():
    payload = BirthService.get_births()
    return jsonify(payload)

@birth_blueprint.route("/get_birth/<id_camada>", methods=['GET'])
def get_birth(id_camada):
    result = BirthService.get_birth(id_camada)
    return jsonify(result)