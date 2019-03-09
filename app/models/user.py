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