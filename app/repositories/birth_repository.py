from app.repositories import db_context
from app.models import Birth
from app.repositories import Utils
from sqlalchemy import text
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound, Forbidden

class BirthRepository:

    @staticmethod
    def create_birth(birth_data : Birth):
        birth_model = BirthRepository._get_birth_model(birth_data.id_camada)
        if birth_model:
            raise Forbidden('Birth already exist')
        db_context.session.add(birth_data)
        db_context.session.commit()

    @staticmethod
    def update_birth(birth_data: Birth):
        birth_model = BirthRepository._get_birth_model(birth_data.id_camada)
        if not birth_model:
            raise NotFound('Birth doesn\'t exist')
        birth_model.identificacion_animal = BirthRepository.value_or_default(birth_data.identificacion_animal, birth_model.identificacion_animal)
        birth_model.fecha_monta = BirthRepository.value_or_default(birth_data.fecha_monta, birth_model.fecha_monta)
        birth_model.tipo_servicio = BirthRepository.value_or_default(birth_data.tipo_servicio, birth_model.tipo_servicio)
        birth_model.identificacion_macho = BirthRepository.value_or_default(birth_data.identificacion_macho, birth_model.identificacion_macho)
        birth_model.fecha_probable_parto = BirthRepository.value_or_default(birth_data.fecha_probable_parto, birth_model.fecha_probable_parto)
        birth_model.fecha_parto = BirthRepository.value_or_default(birth_data.fecha_parto, birth_model.fecha_parto)
        birth_model.jaula_parto = BirthRepository.value_or_default(birth_data.jaula_parto, birth_model.jaula_parto)
        birth_model.numero_lechones_vivos_parto = BirthRepository.value_or_default(birth_data.numero_lechones_vivos_parto, birth_model.numero_lechones_vivos_parto)
        birth_model.numero_lechones_muertos_parto = BirthRepository.value_or_default(birth_data.numero_lechones_muertos_parto, birth_model.numero_lechones_muertos_parto)
        birth_model.numero_machos_parto = BirthRepository.value_or_default(birth_data.numero_machos_parto, birth_model.numero_machos_parto)
        birth_model.numero_hembras_parto = BirthRepository.value_or_default(birth_data.numero_hembras_parto, birth_model.numero_hembras_parto)
        birth_model.numero_momias = BirthRepository.value_or_default(birth_data.numero_momias, birth_model.numero_momias)
        birth_model.peso_total_vivos = BirthRepository.value_or_default(birth_data.peso_total_vivos, birth_model.peso_total_vivos)
        birth_model.fecha_probable_destete = BirthRepository.value_or_default(birth_data.fecha_probable_destete, birth_model.fecha_probable_destete)
        birth_model.fecha_destete = BirthRepository.value_or_default(birth_data.fecha_destete, birth_model.fecha_destete)
        birth_model.numero_hembras_destete = BirthRepository.value_or_default(birth_data.numero_hembras_destete, birth_model.numero_hembras_destete)
        birth_model.numero_machos_destete = BirthRepository.value_or_default(birth_data.numero_machos_destete, birth_model.numero_machos_destete)
        birth_model.numero_muertos_destete = BirthRepository.value_or_default(birth_data.numero_muertos_destete, birth_model.numero_muertos_destete)
        birth_model.dias_lactancia = BirthRepository.value_or_default(birth_data.dias_lactancia, birth_model.dias_lactancia)
        birth_model.peso_total_destete = BirthRepository.value_or_default(birth_data.peso_total_destete, birth_model.peso_total_destete)
        birth_model.jaula_destete = BirthRepository.value_or_default(birth_data.jaula_destete, birth_model.jaula_destete)
        db_context.session.commit()

    @staticmethod
    def value_or_default(value, default):
        return value if value is not None else default

    @staticmethod
    def get_births():
        query_result = db_context.session.query(Birth)\
                .options(joinedload(Birth.animal))\
                .all()
        results = [Birth.serialized for Birth in query_result]
        return results

    @staticmethod
    def get_birth(id_camada: int):
        birth_model = BirthRepository._get_birth_model(id_camada)
        if not birth_model:
            raise NotFound('Birth doesn\'t exist')
        return birth_model.serialized
    

    @staticmethod
    def _get_birth_model(id_camada: int):
        birth_model = db_context.session.query(Birth)\
            .options(joinedload(Birth.animal))\
            .get(id_camada)
        return birth_model