






class ProfileRepository:

    __perfil = []

    @staticmethod
    def create_cagesLitter(perfil_data : PERFIL):
        db_context.session.add(perfil_data)
        db_context.session.commit()

    @staticmethod
    def update_user(perfil_data: PERFIL):
        perfil: PERFIL  = PERFIL.query.filter_by(id_perfil=perfil_data.id_perfil).first()
        if not perfil:
            raise Exception('Profile doesn\'t exist')
        perfil.id_perfil = perfil_data.id_perfil
        perfil.descripcion = perfil_data.descripcion
        db_context.session.commit()