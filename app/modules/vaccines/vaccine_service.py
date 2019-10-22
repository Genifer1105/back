from app.repositories import VaccinesRepository
from app.models import Vaccine

class VaccineService():

    @staticmethod
    def create_vaccine(id_vacuna: int, descripcion: str):
        vaccine = Vaccine(
            id_vacuna=id_vacuna, 
            descripcion=descripcion
        )
        VaccinesRepository.create_vaccine(vaccine)
        vaccine_created = VaccinesRepository.get_vaccine(id_vacuna)
        return vaccine_created
    
    @staticmethod
    def update_vaccine(id_vacuna: int, descripcion: str):
        vaccine = Vaccine(
            id_vacuna=id_vacuna, 
            descripcion=descripcion
        )
        VaccinesRepository.update_vaccine(vaccine)
        vaccine_updated = VaccinesRepository.get_vaccine(id_vacuna)
        return vaccine_updated

    @staticmethod
    def get_vaccines():
        vaccines = VaccinesRepository.get_vaccines()
        return vaccines
    
    @staticmethod
    def get_vaccine(id_vacuna: int):
        vaccine = VaccinesRepository.get_vaccine(id_vacuna)
        return vaccine

