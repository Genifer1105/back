
class TypeService:

   __typeServices = []

    @staticmethod
    def create_typeServices(typeServices_data : TIPOS_SERVICIOS):
        db_context.session.add(typeServices_data)
        db_context.session.commit()

    @staticmethod
    def update_typeServices(typeServices_data: TIPOS_SERVICIOS):
        typeServices: TIPOS_SERVICIOS  = TIPOS_SERVICIOS.query.filter_by(identificacion=user_data.identificacion).first()
        if not user:
            raise Exception('type services doesn\'t exist')
        typeServices.id_tipo_servicio = typeServices_data.id_tipo_servicio
        typeServices.descripcion = typeServices_data.descripcion
      
        db_context.session.commit()