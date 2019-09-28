from flask import Blueprint, jsonify, request
from app.modules.animales import AnimalService

animal_blueprint = Blueprint('/animales', __name__)

@animal_blueprint.route('/create_animal', methods=['POST'])
def create_animal():
    data = request.json
    jsonify(AnimalService.create_animal(data))
    return jsonify({ "success": True })

@animal_blueprint.route("/get_animals", methods=['GET'])
def get_users():
    payload = AnimalService.get_animals()
    return jsonify(payload)