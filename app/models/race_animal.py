from app.repositories import db_context

class RaceAnimal(db_context.Model):


    __tablename__ = "RAZAS"

    id_raza = db_context.Column(db_context.Integer, primary_key=True)
    descripcion = db_context.Column(db_context.String(100), nullable=False)
    # animales = db_context.relationship("Animal", uselist=False, backref="raza", lazy=True)

    @property
    def serialized(self):
        return {
            'id_raza': self.id_raza,
            'descripcion': self.descripcion
        }