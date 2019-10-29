from app.repositories import BirthRepository
from app.models import Birth
from datetime import datetime
from datetime import date
from app.utils import Utils

class BirthService:

    @staticmethod
    def create_birth(
        id_camada: int, identificacion_animal: int, fecha_monta: datetime, 
        tipo_servicio: str, identificacion_macho: int, fecha_probable_parto: datetime, 
        fecha_parto: datetime, jaula_parto: str, numero_lechones_vivos_parto: int, 
        numero_lechones_muertos_parto: int, numero_machos_parto: int, 
        numero_hembras_parto: int, numero_momias: int, peso_total_vivos: int, 
        fecha_probable_destete: datetime, fecha_destete: str, numero_hembras_destete: int, 
        numero_machos_destete: int, numero_muertos_destete: int, dias_lactancia: int, 
        peso_total_destete: int, jaula_destete: str
        ): 
        birth = Birth(
            id_camada=id_camada,
            identificacion_animal=identificacion_animal,
            fecha_monta=fecha_monta,
            tipo_servicio=tipo_servicio,
            identificacion_macho=identificacion_macho,
            fecha_probable_parto=fecha_probable_parto,
            fecha_parto=fecha_parto,
            jaula_parto=jaula_parto,
            numero_lechones_vivos_parto=numero_lechones_vivos_parto,
            numero_lechones_muertos_parto=numero_lechones_muertos_parto,
            numero_machos_parto=numero_machos_parto,
            numero_hembras_parto=numero_hembras_parto,
            numero_momias=numero_momias,
            peso_total_vivos=peso_total_vivos,
            fecha_probable_destete=fecha_probable_destete,
            fecha_destete=fecha_destete,
            numero_hembras_destete=numero_hembras_destete,
            numero_machos_destete=numero_machos_destete,
            numero_muertos_destete=numero_muertos_destete,
            dias_lactancia=dias_lactancia,
            peso_total_destete=peso_total_destete,
            jaula_destete=jaula_destete
        )
        BirthRepository.create_birth(birth)
        birth_created = BirthRepository.get_birth(id_camada)
        return birth_created

    @staticmethod
    def update_birth(
        id_camada: int, identificacion_animal: int, fecha_monta: datetime, 
        tipo_servicio: str, identificacion_macho: int, fecha_probable_parto: datetime, 
        fecha_parto: datetime, jaula_parto: str, numero_lechones_vivos_parto: int, 
        numero_lechones_muertos_parto: int, numero_machos_parto: int, 
        numero_hembras_parto: int, numero_momias: int, peso_total_vivos: int, 
        fecha_probable_destete: datetime, fecha_destete: str, numero_hembras_destete: int, 
        numero_machos_destete: int, numero_muertos_destete: int, dias_lactancia: int, 
        peso_total_destete: int, jaula_destete: str
        ): 
        birth = Birth(
            id_camada=id_camada,
            identificacion_animal=identificacion_animal,
            fecha_monta=fecha_monta,
            tipo_servicio=tipo_servicio,
            identificacion_macho=identificacion_macho,
            fecha_probable_parto=fecha_probable_parto,
            fecha_parto=fecha_parto,
            jaula_parto=jaula_parto,
            numero_lechones_vivos_parto=numero_lechones_vivos_parto,
            numero_lechones_muertos_parto=numero_lechones_muertos_parto,
            numero_machos_parto=numero_machos_parto,
            numero_hembras_parto=numero_hembras_parto,
            numero_momias=numero_momias,
            peso_total_vivos=peso_total_vivos,
            fecha_probable_destete=fecha_probable_destete,
            fecha_destete=fecha_destete,
            numero_hembras_destete=numero_hembras_destete,
            numero_machos_destete=numero_machos_destete,
            numero_muertos_destete=numero_muertos_destete,
            dias_lactancia=dias_lactancia,
            peso_total_destete=peso_total_destete,
            jaula_destete=jaula_destete
        )
        BirthRepository.update_birth(birth)
        birth_updated = BirthRepository.get_birth(id_camada)
        return birth_updated

    @staticmethod
    def get_births():
        return BirthRepository.get_births()

    @staticmethod
    def get_birth(id_camada: int):
        return BirthRepository.get_birth(id_camada)
        
    @staticmethod
    def delete_birth(id_camada: int):
        return BirthRepository.delete_birth(id_camada)
        