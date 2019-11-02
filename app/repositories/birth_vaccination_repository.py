from app.repositories import db_context
from app.models import BirthVaccination
from sqlalchemy import text
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound, Forbidden
from datetime import datetime
from app.repositories import Utils

class BirthVaccinationRepository:

    __animal = []

    @staticmethod
    def create_birth_vaccination(birth_vaccination_data : BirthVaccination):
        birth_vaccination_model = BirthVaccinationRepository._get_birth_vaccination_model(
            birth_vaccination_data.id_camada, 
            birth_vaccination_data.vacuna, 
            birth_vaccination_data.fecha_programada
        )
        if birth_vaccination_model:
            raise Forbidden('Animal Vaccination item already exist')
        db_context.session.add(birth_vaccination_data)
        db_context.session.commit()

    @staticmethod
    def update_birth_vaccination(birth_vaccination_data: BirthVaccination):
        birth_vaccination_model = BirthVaccinationRepository._get_birth_vaccination_model(
            birth_vaccination_data.id_camada, 
            birth_vaccination_data.vacuna, 
            birth_vaccination_data.fecha_programada
        )
        if not birth_vaccination_model:
            raise NotFound('Animal Vaccination item doesn\'t exist')
        birth_vaccination_model.evento =  birth_vaccination_data.evento or birth_vaccination_model.evento
        birth_vaccination_model.fecha_ejecucion =  birth_vaccination_data.fecha_ejecucion or birth_vaccination_model.fecha_ejecucion
        birth_vaccination_model.via_aplicacion =  birth_vaccination_data.via_aplicacion or birth_vaccination_model.via_aplicacion
        birth_vaccination_model.dosis =  birth_vaccination_data.dosis or birth_vaccination_model.dosis
        birth_vaccination_model.laboratorio =  birth_vaccination_data.laboratorio or birth_vaccination_model.laboratorio
        birth_vaccination_model.registro_ica =  birth_vaccination_data.registro_ica or birth_vaccination_model.registro_ica
        birth_vaccination_model.numero_lote =  birth_vaccination_data.numero_lote or birth_vaccination_model.numero_lote
        birth_vaccination_model.tiempo_retiro =  birth_vaccination_data.tiempo_retiro or birth_vaccination_model.tiempo_retiro
        birth_vaccination_model.observaciones =  birth_vaccination_data.observaciones or birth_vaccination_model.observaciones
        db_context.session.commit()

    @staticmethod
    def get_births_vaccinations():
        query_result = db_context.session.query(BirthVaccination)\
                .options(joinedload(BirthVaccination.parto))\
                .all()
        results = [parto.serialized for parto in query_result]
        return results

    @staticmethod
    def get_birth_vaccinations(id_camada: int):
        query_result = db_context.session.query(BirthVaccination)\
            .filter(BirthVaccination.id_camada == id_camada)\
            .all()
        results = [ row.serialized for row in query_result ]
        return results

    @staticmethod
    def get_birth_vaccinations_item(id_camada: int, vacuna: str, fecha_programada):
        birth_model = BirthVaccinationRepository._get_birth_vaccination_model(id_camada, vacuna, fecha_programada)
        return birth_model.serialized

    @staticmethod
    def _get_birth_vaccination_model(id_camada: int, vacuna: str, fecha_programada):
        birth_model = db_context.session.query(BirthVaccination)\
            .options(joinedload(BirthVaccination.parto))\
            .get({
                "id_camada": id_camada,
                "vacuna": vacuna,
                "fecha_programada": fecha_programada
            })
        return birth_model