from app.repositories import db_context

class Animal(db_context.Model):

    __tablename__ = "ANIMALES"

    identificacion_animal = db_context.Column(db_context.Integer,  primary_key=True)
    id_raza = db_context.Column(db_context.Integer, nullable=False)
    fecha_nacimiento = db_context.Column(db_context.Date, nullable=False)
    id_madre = db_context.Column(db_context.Integer, nullable=True)
    id_padre = db_context.Column(db_context.Integer, nullable=True)
    procedencia = db_context.Column(db_context.String(100), nullable=False) 

 