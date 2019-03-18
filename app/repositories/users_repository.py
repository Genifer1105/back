from app.models import User
from app.repositories import Utils
from app.repositories import db_context
from sqlalchemy import text

class UserRepository:

    __users = []

    @staticmethod
    def create_user(user_data):
        db_context.session.add(user_data)
        db_context.session.commit()

    @staticmethod
    def update_user(user_data: User):
        user: User = User.query.filter_by(identificacion=user_data.identificacion).first()
        if not user:
            raise Exception('user doesn\'t exist')
        user.identificacion = user_data.identificacion
        user.nombre = user_data.nombre
        user.apellido1 = user_data.apellido1
        user.apellido2 = user_data.apellido2
        user.correo = user_data.correo
        user.telefono = user_data.telefono
        db_context.session.commit()

    @staticmethod
    def get_users():
        query = text('select u.identificacion, u.nombre, u.apellido1, u.apellido2, u.correo, u.telefono, p.descripcion as perfil, u.id_perfil from mydb.usuario u, mydb.perfil p where u.id_perfil = p.id_perfil')
        result = db_context.engine.execute(query)
        return [Utils.row2dict(user) for user in result]