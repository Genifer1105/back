

class LaboratoryRepository:

    __users = []

    @staticmethod
    def create_user(labotarory_data : LABORATORIOS):
        db_context.session.add(labotarory_data)
        db_context.session.commit()

    @staticmethod
    def update_user(labotarory_data: LABORATORIOS):
        labotarory: LABORATORIOS = LABORATORIOS.query.filter_by(id_laboratorio=labotarory_data.id_laboratorio).first()
        if not labotarory:
            raise Exception('labotarory doesn\'t exist')
        labotarory.id_laboratorio = labotarory_data.id_laboratorio
        labotarory.descripcion = labotarory_data.descripcion
        db_context.session.commit()

