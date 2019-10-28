from app.repositories import AnimalVaccinationRepository
from app.models import AnimalVaccination
from datetime import datetime
from datetime import date
from app.utils import Utils

class AnimalVaccinationService:

    @staticmethod
    def create_animal_vaccination(identificacion_animal: int, vacuna: str, fecha_programada: datetime, evento: str, 
        fecha_ejecucion: datetime, via_aplicacion: str, dosis: int, laboratorio: str, 
        reg_ica: str, nro_lote: str, tiempo_retiro: str, observaciones: str):
        animal_vaccination = AnimalVaccination(
            identificacion_animal=identificacion_animal,
            vacuna=vacuna,
            fecha_programada=fecha_programada,
            evento=evento,
            fecha_ejecucion=fecha_ejecucion,
            via_aplicacion=via_aplicacion,
            dosis=dosis,
            laboratorio=laboratorio,
            reg_ica=reg_ica,
            nro_lote=nro_lote,
            tiempo_retiro=tiempo_retiro,
            observaciones=observaciones
        )
        AnimalVaccinationRepository.create_animal_vaccination(animal_vaccination)
        animal_created = AnimalVaccinationRepository.get_animal_vaccinations(identificacion_animal)
        return animal_created

    @staticmethod
    def update_animal_vaccination(identificacion_animal: int, raza: str, id_madre: int, id_padre: int, procedencia: int, fecha_nacimiento_date: date):
        animal_data = Animal(
            identificacion_animal=identificacion_animal,
            raza=raza,
            fecha_nacimiento=fecha_nacimiento_date,
            id_madre=id_madre,
            id_padre=id_padre,
            procedencia=procedencia
        )
        AnimalRepository.update_animal(animal_data)
        animal_updated = AnimalRepository.get_animal(identificacion_animal)
        return animal_updated

    @staticmethod
    def get_animals_vaccinations():
        return AnimalRepository.get_animals()

    @staticmethod
    def get_animal_vaccinations(identificacion_animal: int):
        return AnimalRepository.get_animal(identificacion_animal)
