





class viaApplication:

    __viaApplication = []

    @staticmethod
    def create_cagesLitter(viaApplication_data : VIAS_APLICACION):
        db_context.session.add(viaApplication_data)
        db_context.session.commit()

    @staticmethod
    def update_user(viaApplication_data: VIAS_APLICACION):
        viaApplication_data: VIAS_APLICACION  = VIAS_APLICACION.query.filter_by(id_jaula_parto=cagesBirths_data.id_jaula_parto).first()
        if not viaApplication:
            raise Exception('Cage birth doesn\'t exist')
        viaApplication.id_via_aplicacion = viaApplication_data.id_via_aplicacion
        viaApplication.descripcion = viaApplication_data.descripcion
        db_context.session.commit()