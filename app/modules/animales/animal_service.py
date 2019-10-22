from app.repositories import AnimalRepository
from app.models import Animal
from datetime import datetime
from datetime import date
from app.utils import Utils

class AnimalService:

    @staticmethod
    def create_animal(identificacion_animal: int, id_raza: int, id_madre: int, id_padre: int, procedencia: int, fecha_nacimiento_date: date):
        animal = Animal(
            identificacion_animal=identificacion_animal,
            id_raza=id_raza,
            fecha_nacimiento=fecha_nacimiento_date,
            id_madre=id_madre,
            id_padre=id_padre,
            procedencia=procedencia
        )
        AnimalRepository.create_animal(animal)
        animal_created = AnimalRepository.get_animal(identificacion_animal)
        return animal_created

    @staticmethod
    def update_animal(identificacion_animal: int, id_raza: int, id_madre: int, id_padre: int, procedencia: int, fecha_nacimiento_date: date):
        animal_data = Animal(
            identificacion_animal=identificacion_animal,
            id_raza=id_raza,
            fecha_nacimiento=fecha_nacimiento_date,
            id_madre=id_madre,
            id_padre=id_padre,
            procedencia=procedencia
        )
        AnimalRepository.update_animal(animal_data)
        animal_updated = AnimalRepository.get_animal(identificacion_animal)
        return animal_updated

    @staticmethod
    def get_animals():
        return AnimalRepository.get_animals()

    @staticmethod
    def get_animal(identificacion_animal: int):
        return AnimalRepository.get_animal(identificacion_animal)
        

    @staticmethod
    def __validate_animal_data(identificacion_animal, id_raza, fecha_nacimiento, id_madre, id_padre, procedencia):
        return (
            isinstance(identificacion_animal, int)
            and isinstance(id_raza, int)
            and isinstance(fecha_nacimiento, date)
            and (id_madre is None or isinstance(id_madre, int))
            and (id_padre is None or isinstance(id_padre, int))
            and isinstance(procedencia, str)
        )