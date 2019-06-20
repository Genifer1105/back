from app.repositories import db_context

class typesService(db_context.Model):

    __tablename__ = "Tipo_Servicio "

    id_tipo_servicio = db_context.Column(db_context.Integer, primary_key=True)
    descripcion = db_context.Column(db_context.String(100), nullable=False)