from app.repositories import db_context
from app.models import Animal
from app.repositories import Utils
from sqlalchemy import text

class AnimalRepository:

    __animal = []

    @staticmethod
    def create_animal(animal_data : Animal):
        print('TYPE', type(animal_data))
        db_context.session.add(animal_data)
        db_context.session.commit()

    @staticmethod
    def update_animal(animal_data: Animal):
        animal: Animal = Animal.query.filter_by(identificacion_animal = animal_data.ntificacion_animal).first()
        if not animal:
            raise Exception('Animal doesn\'t exist')
        animal.identificacion_animal = animal_data.identificacion_animal
        animal.id_raza = animal_data.id_raza
        animal.fecha_nacimiento = animal_data.fecha_nacimiento
        animal.id_madre = animal_data.id_madre
        animal.id_padre = animal_data.id_padre
        animal.procedencia = animal_data.procedencia
        db_context.session.commit()

    @staticmethod
    def get_animals():
        query = text('select a.identificacion_animal, a.id_raza, a.fecha_nacimiento, a.id_madre, a.id_padre, a.procedencia, r.descripcion as descripcion_raza from ppi.animales a, ppi.razas r where r.id_raza = a.id_raza')
        result = db_context.engine.execute(query)
        return [Utils.row2dict(animal) for animal in result]
    