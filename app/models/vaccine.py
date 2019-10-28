from app.repositories import db_context

class Vaccine(db_context.Model):


    __tablename__ = "VACUNA"

    id_vacuna = db_context.Column(db_context.Integer, primary_key=True)
    descripcion = db_context.Column(db_context.String(100), nullable=False)

    @property
    def serialized(self):
        return {
            'id_vacuna': self.id_vacuna,
            'descripcion': self.descripcion
        }