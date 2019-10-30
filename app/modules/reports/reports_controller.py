from flask import Blueprint
from app.modules.reports import ReportsService

reports_bluerpint = Blueprint('/reports', __name__)

@reports_bluerpint.route('/born_by_animals', methods=['GET'])
def default_report():
    return ReportsService.alive_animals_per_birth()