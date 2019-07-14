from app.repositories import db_context

class cagesBirth(db_context.Model):


    __tablename__ = "JAULAS_PARTOS"

    id_jaula_parto = db_context.Column(db_context.Integer, primary_key=True)
    descripcion = db_context.Column(db_context.String(100), nullable=False)