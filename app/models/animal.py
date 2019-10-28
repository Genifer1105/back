from app.repositories import db_context

class Animal(db_context.Model):

    __tablename__ = "ANIMAL"

    identificacion_animal = db_context.Column(db_context.Integer,  primary_key=True)
    raza = db_context.Column(db_context.String(100), nullable=False)
    fecha_nacimiento = db_context.Column(db_context.Date, nullable=False)
    id_madre = db_context.Column(db_context.Integer, db_context.ForeignKey('ANIMAL.identificacion_animal'), nullable=True)
    id_padre = db_context.Column(db_context.Integer, db_context.ForeignKey('ANIMAL.identificacion_animal'), nullable=True)
    procedencia = db_context.Column(db_context.String(100), nullable=False)
    madre = db_context.relationship("Animal", foreign_keys="Animal.id_madre", backref="ANIMAL", uselist=False, lazy="noload")
    padre = db_context.relationship("Animal", foreign_keys="Animal.id_padre", backref="ANIMAL", uselist=False, lazy="noload")
    
    @property
    def serialized(self):
        return {
            'identificacion_animal': self.identificacion_animal,
            'raza': self.raza,
            'fecha_nacimiento': self.fecha_nacimiento,
            'id_madre': self.id_madre,
            'id_padre': self.id_padre,
            'procedencia': self.procedencia,
            'madre': self.padre.serialized if self.padre else None,
            'padre': self.padre.serialized if self.padre else None
        }