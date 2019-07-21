from app.repositories import db_context

class ViaApplication(db_context.Model):


    __tablename__ = "VIAS_APLICACION"

    id_via_aplicacion = db_context.Column(db_context.Integer, primary_key=True)
    descripcion = db_context.Column(db_context.String(100), nullable=False)