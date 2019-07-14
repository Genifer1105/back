from app.repositories import db_context

class laboratory(db_context.Model):

    __tablename__ = "LABORATORIOS"

    id_laboratorio = db_context.Column(db_context.Integer, primary_key=True)
    descripcion = db_context.Column(db_context.String(100), nullable=False)