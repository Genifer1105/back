from app.repositories import db_context

class raceAnimal(db_context.Model):


    __tablename__ = "RAZAS"

    id_raza = db_context.Column(db_context.Integer, primary_key=True)
    descripcion = db_context.Column(db_context.String(100), nullable=False)