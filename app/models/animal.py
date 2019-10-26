from app.repositories import db_context

class Animal(db_context.Model):

    __tablename__ = "ANIMALES"

    identificacion_animal = db_context.Column(db_context.Integer,  primary_key=True)
    id_raza = db_context.Column(db_context.Integer, db_context.ForeignKey('RAZAS.id_raza'), nullable=False)
    fecha_nacimiento = db_context.Column(db_context.Date, nullable=False)
    id_madre = db_context.Column(db_context.Integer, nullable=True)
    id_padre = db_context.Column(db_context.Integer, nullable=True)
    procedencia = db_context.Column(db_context.String(100), nullable=False)
    raza = db_context.relationship('RaceAnimal', backref="ANIMALES", uselist=False, lazy='noload')
    
    @property
    def serialized(self):
        return {
            'identificacion_animal': self.identificacion_animal,
            'id_raza': self.id_raza,
            'fecha_nacimiento': self.fecha_nacimiento,
            'id_madre': self.id_madre,
            'id_padre': self.id_padre,
            'procedencia': self.procedencia,
            'raza': self.raza.serialized if self.raza else None
        }