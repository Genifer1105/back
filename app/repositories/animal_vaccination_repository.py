from app.repositories import db_context
from app.models import AnimalVaccination
from sqlalchemy import text
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound, Forbidden
from datetime import datetime
from app.repositories import Utils

class AnimalVaccinationRepository:

    __animal = []

    @staticmethod
    def create_animal_vaccination(animal_vaccination_data : AnimalVaccination):
        animal_vaccination_model = AnimalVaccinationRepository._get_animal_vaccination_model(
            animal_vaccination_data.identificacion_animal, 
            animal_vaccination_data.vacuna, 
            animal_vaccination_data.fecha_programada
        )
        if animal_vaccination_model:
            raise Forbidden('Animal Vaccination item already exist')
        db_context.session.add(animal_vaccination_data)
        db_context.session.commit()

    @staticmethod
    def update_animal_vaccination(animal_vaccination_data: AnimalVaccination):
        animal_vaccination_model = AnimalVaccinationRepository._get_animal_vaccination_model(
            animal_vaccination_data.identificacion_animal, 
            animal_vaccination_data.vacuna, 
            animal_vaccination_data.fecha_programada
        )
        if not animal_vaccination_model:
            raise NotFound('Animal Vaccination item doesn\'t exist')
        animal_vaccination_model.evento =  animal_vaccination_data.evento or animal_vaccination_model.evento
        animal_vaccination_model.fecha_ejecucion =  animal_vaccination_data.fecha_ejecucion or animal_vaccination_model.fecha_ejecucion
        animal_vaccination_model.via_aplicacion =  animal_vaccination_data.via_aplicacion or animal_vaccination_model.via_aplicacion
        animal_vaccination_model.dosis =  animal_vaccination_data.dosis or animal_vaccination_model.dosis
        animal_vaccination_model.laboratorio =  animal_vaccination_data.laboratorio or animal_vaccination_model.laboratorio
        animal_vaccination_model.registro_ica =  animal_vaccination_data.registro_ica or animal_vaccination_model.registro_ica
        animal_vaccination_model.numero_lote =  animal_vaccination_data.numero_lote or animal_vaccination_model.numero_lote
        animal_vaccination_model.tiempo_retiro =  animal_vaccination_data.tiempo_retiro or animal_vaccination_model.tiempo_retiro
        animal_vaccination_model.observaciones =  animal_vaccination_data.observaciones or animal_vaccination_model.observaciones
        db_context.session.commit()

    @staticmethod
    def get_animals_vaccinations():
        query_result = db_context.session.query(AnimalVaccination)\
                .options(joinedload(AnimalVaccination.animal))\
                .all()
        results = [animal.serialized for animal in query_result]
        return results

    @staticmethod
    def get_animal_vaccinations(identificacion_animal: int):
        query_result = db_context.session.query(AnimalVaccination)\
            .filter(AnimalVaccination.identificacion_animal == identificacion_animal)\
            .all()
        results = [ row.serialized for row in query_result ]
        return results

    @staticmethod
    def get_animal_vaccinations_item(identificacion_animal: int, vacuna: str, fecha_programada):
        animal_model = AnimalVaccinationRepository._get_animal_vaccination_model(identificacion_animal, vacuna, fecha_programada)
        return animal_model.serialized

    @staticmethod
    def _get_animal_vaccination_model(identificacion_animal: int, vacuna: str, fecha_programada):
        animal_model = db_context.session.query(AnimalVaccination)\
            .options(joinedload(AnimalVaccination.animal))\
            .get({
                "identificacion_animal": identificacion_animal,
                "vacuna": vacuna,
                "fecha_programada": fecha_programada
            })
        return animal_model