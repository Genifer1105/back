from app.repositories import db_context

class Vaccines(db_context.Model):


    __tablename__ = "VACUNAS"

    id_vacuna = db_context.Column(db_context.Integer, primary_key=True)
    descripcion = db_context.Column(db_context.String(100), nullable=False)