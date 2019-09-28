from app.repositories import AnimalRepository
from app.models import Animal
from datetime import datetime
from datetime import date

class AnimalService:

    @staticmethod
    def create_animal(animal_data: dict):
        identificacion_animal = animal_data.get('identificacion_animal')
        id_raza = animal_data.get('id_raza')
        fecha_nacimiento = animal_data.get('fecha_nacimiento')
        id_madre = animal_data.get('id_madre')
        id_padre = animal_data.get('id_padre')
        procedencia = animal_data.get('procedencia')
        fecha_date = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
        if (not AnimalService.__validate_animal_data(identificacion_animal, id_raza, fecha_date, id_madre, id_padre, procedencia)):
            raise Exception('invalid arguments')
        animal = Animal(
            identificacion_animal=identificacion_animal,
            id_raza=id_raza,
            fecha_nacimiento=fecha_date,
            id_madre=id_madre,
            id_padre=id_padre,
            procedencia=procedencia
        )
        AnimalRepository.create_animal(animal)

    @staticmethod
    def update_animal(animal_data: dict):
        identificacion_animal = animal_data.get('identificacion_animal')
        id_raza = animal_data.get('id_raza')
        fecha_nacimiento = animal_data.get('fecha_nacimiento')
        id_madre = animal_data.get('id_madre')
        id_padre = animal_data.get('id_padre')
        procedencia = animal_data.get('procedencia')
        fecha_date = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
        if (not AnimalService.__validate_animal_data(identificacion_animal, id_raza, fecha_date, id_madre, id_padre, procedencia)):
            raise Exception('invalid arguments')
        animal = Animal(
            identificacion_animal=identificacion_animal,
            id_raza=id_raza,
            fecha_nacimiento=fecha_date,
            id_madre=id_madre,
            id_padre=id_padre,
            procedencia=procedencia
        )

    @staticmethod
    def get_animals():
        return AnimalRepository.get_animals()
        

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