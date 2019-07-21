from app.repositories import db_context

class TypesService(db_context.Model):

    __tablename__ = "TIPOS_SERVICIOS "

    id_tipo_servicio = db_context.Column(db_context.Integer, primary_key=True)
    descripcion = db_context.Column(db_context.String(100), nullable=False)