from flask import Blueprint, jsonify, request
from app.modules.vaccines import VaccineService
from app.utils import Utils
from werkzeug.exceptions import BadRequest

vaccines_blueprint = Blueprint('/vaccines', __name__)

@vaccines_blueprint.route('/create_vaccine', methods=['POST'])
def create_vaccine():
    data = request.json
    if not data:
        raise BadRequest()
    id_vacuna = Utils.validate_json_field(data, 'id_vacuna', True, int)
    descripcion = Utils.validate_json_field(data, 'descripcion', True, str)
    vaccine_created = VaccineService.create_vaccine(id_vacuna, descripcion)
    return jsonify({ "success": True, "data": vaccine_created })

@vaccines_blueprint.route('/update_vaccine/<id_vacuna>', methods=['PUT'])
def update_vaccine(id_vacuna):
    data = request.json
    if not data:
        raise BadRequest()
    descripcion = Utils.validate_json_field(data, 'descripcion', True, str)
    vaccine_updated = VaccineService.update_vaccine(id_vacuna, descripcion)
    return jsonify({ "success": True, "data": vaccine_updated })

@vaccines_blueprint.route('/get_vaccine/<id_vacuna>', methods=['GET'])
def get_vaccine(id_vacuna):
    payload = VaccineService.get_vaccine(id_vacuna)
    return jsonify(payload)

@vaccines_blueprint.route('/get_vaccines', methods=['GET'])
def get_vaccines():
    payload = VaccineService.get_vaccines()
    return jsonify(payload)
