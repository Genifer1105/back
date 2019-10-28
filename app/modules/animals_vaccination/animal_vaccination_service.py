from app.repositories import AnimalVaccinationRepository
from app.models import AnimalVaccination
from datetime import datetime
from datetime import date
from app.utils import Utils

class AnimalVaccinationService:

    @staticmethod
    def create_animal_vaccination(identificacion_animal: int, vacuna: str, fecha_programada: datetime, evento: str, 
        fecha_ejecucion: datetime, via_aplicacion: str, dosis: int, laboratorio: str, 
        registro_ica: str, numero_lote: str, tiempo_retiro: str, observaciones: str):
        animal_vaccination = AnimalVaccination(
            identificacion_animal=identificacion_animal,
            vacuna=vacuna,
            fecha_programada=fecha_programada,
            evento=evento,
            fecha_ejecucion=fecha_ejecucion,
            via_aplicacion=via_aplicacion,
            dosis=dosis,
            laboratorio=laboratorio,
            registro_ica=registro_ica,
            numero_lote=numero_lote,
            tiempo_retiro=tiempo_retiro,
            observaciones=observaciones
        )
        AnimalVaccinationRepository.create_animal_vaccination(animal_vaccination)
        animal_created = AnimalVaccinationRepository.get_animal_vaccinations_item(identificacion_animal, vacuna, fecha_programada)
        return animal_created

    @staticmethod
    def update_animal_vaccination(identificacion_animal: int, vacuna: str, fecha_programada: datetime, evento: str, 
        fecha_ejecucion: datetime, via_aplicacion: str, dosis: int, laboratorio: str, 
        registro_ica: str, numero_lote: str, tiempo_retiro: str, observaciones: str):
        animal_vaccination = AnimalVaccination(
            identificacion_animal=identificacion_animal,
            vacuna=vacuna,
            fecha_programada=fecha_programada,
            evento=evento,
            fecha_ejecucion=fecha_ejecucion,
            via_aplicacion=via_aplicacion,
            dosis=dosis,
            laboratorio=laboratorio,
            registro_ica=registro_ica,
            numero_lote=numero_lote,
            tiempo_retiro=tiempo_retiro,
            observaciones=observaciones
        )
        AnimalVaccinationRepository.update_animal_vaccination(animal_vaccination)
        animal_created = AnimalVaccinationRepository.get_animal_vaccinations_item(identificacion_animal, vacuna, fecha_programada)
        return animal_created

    @staticmethod
    def get_animals_vaccinations():
        return AnimalVaccinationRepository.get_animals_vaccinations()

    @staticmethod
    def get_animal_vaccination_item(identificacion_animal: int, vacuna: str, fecha_programada: datetime):
        return AnimalVaccinationRepository.get_animal_vaccinations_item(identificacion_animal, vacuna, fecha_programada)

    @staticmethod
    def get_animal_vaccinations(identificacion_animal: int):
        return AnimalVaccinationRepository.get_animal_vaccinations(identificacion_animal)
