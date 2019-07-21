



class CagesBirthsRepository:

    __cagesBirths = []

    @staticmethod
    def create_cagesLitter(cagesBirths_data : JAULAS_PARTOS):
        db_context.session.add(cagesBirths_data)
        db_context.session.commit()

    @staticmethod
    def update_user(cagesBirths_data: JAULAS_PARTOS):
        cagesBirths: JAULAS_PARTOS  = JAULAS_PARTOS.query.filter_by(id_jaula_parto=cagesBirths_data.id_jaula_parto).first()
        if not cagesBirths:
            raise Exception('Cage birth doesn\'t exist')
        cagesBirths.id_jaula_parto = cagesBirths_data.id_jaula_parto
        cagesBirths.descripcion = cagesBirths_data.descripcion
             db_context.session.commit()