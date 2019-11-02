from app.repositories import db_context

class User(db_context.Model):


    __tablename__ = "Usuario"

    identificacion = db_context.Column(db_context.Integer, primary_key=True)
    nombre = db_context.Column(db_context.String(100), nullable=False)
    apellido1 = db_context.Column(db_context.String(100), nullable=False)
    apellido2 = db_context.Column(db_context.String(100), nullable=True)
    correo = db_context.Column(db_context.String(200), nullable=False)
    telefono = db_context.Column(db_context.String(20), nullable=True)
    contrasena = db_context.Column(db_context.String(20), nullable=True)
    id_perfil = db_context.Column(db_context.Integer, nullable=False)

    @property
    def serialized(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "apellido1": self.apellido1,
            "apellido2": self.apellido2,
            "correo": self.correo,
            "telefono": self.telefono,
            "id_perfil": self.id_perfil,
            "contrasena": self.contrasena
        }