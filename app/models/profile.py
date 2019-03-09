from app.repositories import db_context

class Profile(db_context.Model):


    __tablename__ = "Perfil"

    id_perfil = db_context.Column(db_context.Integer, primary_key=True)
    descripcion = db_context.Column(db_context.String(100), nullable=False)