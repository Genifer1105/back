from app.repositories import db_context

class Animal(db_context.Model):

    __tablename__ = "ANIMAL"

    identificacion_animal = db_context.Column(db_context.Integer,  primary_key=True)
    raza = db_context.Column(db_context.String(100), nullable=False)
    fecha_nacimiento = db_context.Column(db_context.Date, nullable=False)
    procedencia = db_context.Column(db_context.String(100), nullable=False)
    id_madre = db_context.Column(db_context.Integer, db_context.ForeignKey('ANIMAL.identificacion_animal'), nullable=True)
    id_padre = db_context.Column(db_context.Integer, db_context.ForeignKey('ANIMAL.identificacion_animal'), nullable=True)    
    # madre = db_context.relationship("Animal", foreign_keys=[id_madre], uselist=False, lazy="noload", remote_side="Animal.identificacion_animal")
    # padre = db_context.relationship("Animal", foreign_keys=[id_padre], uselist=False, lazy="noload", remote_side="Animal.identificacion_animal")
    
    @property
    def serialized(self):
        return {
            'identificacion_animal': self.identificacion_animal,
            'raza': self.raza,
            'fecha_nacimiento': self.fecha_nacimiento,
            'id_madre': self.id_madre,
            'id_padre': self.id_padre,
            'procedencia': self.procedencia,
            # 'madre': self.madre.serialized if self.madre else None,
            # 'padre': self.padre.serialized if self.padre else None
        }

    