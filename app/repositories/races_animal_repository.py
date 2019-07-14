




class cagesBirthsRepository:

    __races = []

    @staticmethod
    def create_cagesLitter(races_data : RAZAS):
        db_context.session.add(races_data)
        db_context.session.commit()

    @staticmethod
    def update_user(cagesBirths_data: RAZAS):
        races: RAZAS = RAZAS.query.filter_by(id_jaula_parto=races_data.id_jaula_parto).first()
        if not races:
            raise Exception('Race doesn\'t exist')
        races.id_raza = races_data.id_raza
        races.descripcion = races_data.descripcion
             db_context.session.commit()