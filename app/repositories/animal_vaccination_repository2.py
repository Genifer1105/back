from app.models import AnimalVaccination
from app.repositories import db_context
from datetime import datetime
from werkzeug.exceptions import NotFound, Forbidden

class AnimalVaccinationRepository:

    __animal_vaccination = []

    @staticmethod
    def create_animal_vaccination(animal_vaccination_data: AnimalVaccination):
        animal_vaccination_model = AnimalVaccinationRepository._get_animal_vaccination_model(
            animal_vaccination_data.identificacion_animal,
            animal_vaccination_data.id_vacuna,
            animal_vaccination_data.fecha_programada
        )
        if animal_vaccination_model:
            raise Forbidden('This animal vaccination data already exists')
        db_context.session.add(animal_vaccination_data)
        db_context.session.commit()
        
    @staticmethod
    def update_animal_vaccination(animal_vaccination_data: AnimalVaccination):
        animal_vaccination = AnimalVaccinationRepository._get_animal_vaccination_model(
            animal_vaccination_data.identificacion_animal,
            animal_vaccination_data.id_vacuna,
            animal_vaccination_data.fecha_programada
        )
        if not animal_vaccination:
            raise NotFound('Vaccination doesn\'t exist')
        animal_vaccination.identificacion_animal =  animal_vaccination_data.identificacion_animal
        animal_vaccination.id_vacuna =  animal_vaccination_data.id_vacuna
        animal_vaccination.fecha_programada =  animal_vaccination_data.fecha_programada
        animal_vaccination.evento =  animal_vaccination_data.evento
        animal_vaccination.fecha_ejecucion =  animal_vaccination_data.fecha_ejecucion
        animal_vaccination.id_via_aplicacion =  animal_vaccination_data.id_via_aplicacion
        animal_vaccination.dosis =  animal_vaccination_data.dosis
        animal_vaccination.id_laboratorio =  animal_vaccination_data.id_laboratorio
        animal_vaccination.reg_ica =  animal_vaccination_data.reg_ica
        animal_vaccination.nro_lote =  animal_vaccination_data.nro_lote
        animal_vaccination.tiempo_retiro =  animal_vaccination_data.tiempo_retiro
        animal_vaccination.observaciones =  animal_vaccination_data.observaciones
        db_context.session.commit()


    @staticmethod
    def get_animal_vaccinations():
        result_query = db_context.session.query(AnimalVaccination).all()
        return [animal_vaccination_item.serialized for animal_vaccination_item in result_query]

    @staticmethod
    def get_animal_vaccination_data(identificacion_animal: int, id_vacuna: int, fecha_programada: datetime):
        animal_vaccination_model = AnimalVaccinationRepository._get_animal_vaccination_model(
            identificacion_animal,
            id_vacuna,
            fecha_programada
        )
        return animal_vaccination_model.serialized

    @staticmethod
    def _get_animal_vaccination_model(identificacion_animal: int, id_vacuna: int, fecha_programada: datetime):
        animal_vaccination_model = db_context.session.query(AnimalVaccination)\
            .get({
                "identificacion_animal": identificacion_animal, 
                "id_vacuna": id_vacuna,
                "fecha_programada": fecha_programada 
            })
        return animal_vaccination_model