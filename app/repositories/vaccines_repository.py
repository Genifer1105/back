from app.models import Vaccine
from werkzeug.exceptions import NotFound, Forbidden
from app.repositories import db_context

class VaccinesRepository:

    @staticmethod
    def create_vaccine(vaccine_data : Vaccine):
        vaccine_model = VaccinesRepository._get_vaccine_model(vaccine_data.id_vacuna)
        if vaccine_model:
            raise Forbidden('Vaccine already exist')
        db_context.session.add(vaccine_data)
        db_context.session.commit()


    @staticmethod
    def update_vaccine(vaccine_data: Vaccine):
        vaccine_model = VaccinesRepository._get_vaccine_model(vaccine_data.id_vacuna)
        if not vaccine_model:
            raise NotFound('vaccine doesn\'t exist')
        vaccine_model.descripcion = vaccine_data.descripcion or vaccine_model.descripcion
        db_context.session.commit()

    @staticmethod
    def get_vaccines():
        query_result = db_context.session.query(Vaccine).all()
        return [vaccine.serialized for vaccine in query_result]

    @staticmethod
    def get_vaccine(id_vacuna: int):
        vaccine_model = VaccinesRepository._get_vaccine_model(id_vacuna)
        if not vaccine_model:
            raise NotFound('vaccine doesn\'t exist')
        return vaccine_model.serialized

    @staticmethod
    def _get_vaccine_model(id_vacuna: int):
        vaccine_model = db_context.session.query(Vaccine).get(id_vacuna)
        return vaccine_model

    