from app.models import AnimalVaccination
from app.repositories import db_context
from datetime import datetime
from werkzeug.exceptions import NotFound, Forbidden
class AnimalVaccinationRepository:

    __animalVaccination = []

    @staticmethod
    def create_animalVaccination(animal_vaccination_data: AnimalVaccination):
        db_context.session.add(animal_vaccination_data)
        db_context.session.commit()
        
    @staticmethod
    def update_animalVaccination(animalVaccination_data: AnimalVaccination):
        animal_vaccionation = AnimalVaccinationRepository._get_animal_vaccination_model(
            animalVaccination_data.identificacion_animal,
            animalVaccination_data.id_vacuna,
            animalVaccination_data.fecha_programada
        )
        if not animalVaccination:
            raise NotFound('Vaccination doesn\'t exist')
        animalVaccination.identificacion_animal =  animalVaccination_data.identificacion_animal
        animalVaccination.id_vacuna =  animalVaccination_data.id_vacuna
        animalVaccination.fecha_programada =  animalVaccination_data.fecha_programada
        animalVaccination.evento =  animalVaccination_data.evento
        animalVaccination.fecha_ejecucion =  animalVaccination_data.fecha_ejecucion
        animalVaccination.id_via_aplicacion =  animalVaccination_data.id_via_aplicacion
        animalVaccination.dosis =  animalVaccination_data.dosis
        animalVaccination.id_laboratorio =  animalVaccination_data.id_laboratorio
        animalVaccination.reg_ica =  animalVaccination_data.reg_ica
        animalVaccination.nro_lote =  animalVaccination_data.nro_lote
        animalVaccination.tiempo_retiro =  animalVaccination_data.tiempo_retiro
        animalVaccination.observaciones =  animalVaccination_data.observaciones
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