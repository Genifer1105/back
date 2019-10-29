from app.repositories import db_context
from app.models import Animal, Birth, BirthVaccination, AnimalVaccination
from app.repositories import Utils
from sqlalchemy import text, or_
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound, Forbidden

class AnimalRepository:

    __animal = []

    @staticmethod
    def create_animal(animal_data : Animal):
        animal_model = AnimalRepository._get_animal_model(animal_data.identificacion_animal)
        if animal_model:
            raise Forbidden('Animal already exist')
        db_context.session.add(animal_data)
        db_context.session.commit()

    @staticmethod
    def update_animal(animal_data: Animal):
        animal_model = AnimalRepository._get_animal_model(animal_data.identificacion_animal)
        if not animal_model:
            raise NotFound('Animal doesn\'t exist')
        animal_model.raza = animal_data.raza or animal_model.raza
        animal_model.fecha_nacimiento = animal_data.fecha_nacimiento or animal_model.fecha_nacimiento
        animal_model.id_madre = animal_data.id_madre or animal_model.id_madre
        animal_model.id_padre = animal_data.id_padre or animal_model.id_padre
        animal_model.procedencia = animal_data.procedencia or animal_model.procedencia
        db_context.session.commit()

    @staticmethod
    def get_animals():
        query_result = db_context.session.query(Animal)\
                .all()
        results = [animal.serialized for animal in query_result]
        return results

    @staticmethod
    def get_animal(identificacion_animal: int):
        animal_model = AnimalRepository._get_animal_model(identificacion_animal)
        if not animal_model:
            raise NotFound('Animal doesn\'t exist')
        return animal_model.serialized
    
    @staticmethod
    def delete_animal(identificacion_animal: int):
        animal_model = AnimalRepository._get_animal_model(identificacion_animal)
        if not animal_model:
            raise NotFound('Animal doesn\'t exist')
        db_context.session.delete(animal_model)
        db_context.session.commit()


    @staticmethod
    def _get_animal_model(identificacion_animal: int):
        animal_model = db_context.session.query(Animal)\
            .get(identificacion_animal)
        return animal_model