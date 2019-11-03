from app.repositories import BirthVaccinationRepository
from app.models import BirthVaccination
from datetime import datetime
from datetime import date
from app.utils import Utils

class BirthVaccinationService:

    @staticmethod
    def create_birth_vaccination(id_camada: int, vacuna: str, fecha_programada: datetime, evento: str, 
        fecha_ejecucion: datetime, via_aplicacion: str, dosis: int, laboratorio: str, 
        registro_ica: str, numero_lote: str, tiempo_retiro: str, observaciones: str):
        birth_vaccination = BirthVaccination(
            id_camada=id_camada,
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
        BirthVaccinationRepository.create_birth_vaccination(birth_vaccination)
        birth_created = BirthVaccinationRepository.get_birth_vaccinations_item(id_camada, vacuna, fecha_programada)
        return birth_created

    @staticmethod
    def update_birth_vaccination(id_camada: int, vacuna: str, fecha_programada: datetime, evento: str, 
        fecha_ejecucion: datetime, via_aplicacion: str, dosis: int, laboratorio: str, 
        registro_ica: str, numero_lote: str, tiempo_retiro: str, observaciones: str):
        birth_vaccination = BirthVaccination(
            id_camada=id_camada,
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
        BirthVaccinationRepository.update_birth_vaccination(birth_vaccination)
        birth_created = BirthVaccinationRepository.get_birth_vaccinations_item(id_camada, vacuna, fecha_programada)
        return birth_created

    @staticmethod
    def get_births_vaccinations():
        return BirthVaccinationRepository.get_births_vaccinations()

    @staticmethod
    def get_birth_vaccination_item(id_camada: int, vacuna: str, fecha_programada: datetime):
        return BirthVaccinationRepository.get_birth_vaccinations_item(id_camada, vacuna, fecha_programada)

    @staticmethod
    def get_birth_vaccinations(id_camada: int):
        return BirthVaccinationRepository.get_birth_vaccinations(id_camada)
