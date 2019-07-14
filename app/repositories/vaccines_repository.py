

class VaccinesRepository:

    __vaccines = []

 @staticmethod
    def create_vaccines(vaccines_data : VACUNAS):
        db_context.session.add(vaccines_data)
        db_context.session.commit()


    @staticmethod
    def update_vaccines(vaccines_data: VACUNAS):
        vaccines: VACUNAS = VACUNAS.query.filter_by(id_vacuna=vaccines_data.id_vacuna).first()
        if not vaccines:
            raise Exception('vaccines doesn\'t exist')
            vaccines.id_vacuna = vaccines_data.id_vacuna
            vaccines.descripcion = vaccines_data.descripcion
            db_context.session.commit()

    