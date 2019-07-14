




class cagesLittersRepository:

    __cagesLitters = []

    @staticmethod
    def create_cagesLitter(user_data : JAULAS_DESTETES):
        db_context.session.add(cagesLitters_data)
        db_context.session.commit()

    @staticmethod
    def update_user(cagesLitters_data: JAULAS_DESTETES):
        cagesLitters: JAULAS_DESTETES  = JAULAS_DESTETES.query.filter_by(id_jaula_destete=cagesLitters_data.id_jaula_destete).first()
        if not cagesLitters:
            raise Exception('Cage litter doesn\'t exist')
        cagesLitters.id_jaula_destete = cagesLitters_data.id_jaula_destete
        cagesLitters.descripcion = cagesLitters_data.descripcion
             db_context.session.commit()