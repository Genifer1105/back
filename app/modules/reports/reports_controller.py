from flask import Blueprint
from app.modules.reports import ReportsService

reports_bluerpint = Blueprint('/reports', __name__)

@reports_bluerpint.route('/born_by_animals', methods=['GET'])
def born_by_animals():
    return ReportsService.alive_animals_per_birth()

@reports_bluerpint.route('/born_alive_per_month', methods=['GET'])
def born_alive_per_month():
    return ReportsService.alive_animals_per_month()

@reports_bluerpint.route('/born_dead_per_month', methods=['GET'])
def born_dead_per_month():
    return ReportsService.dead_animals_per_month()