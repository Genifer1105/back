from app.models import User
from app.repositories import Utils
from app.repositories import db_context
from sqlalchemy import text, or_
from werkzeug.exceptions import NotFound

class UserRepository:

    __users = []

    @staticmethod
    def create_user(user_data : User):
        print('create_user', User.identificacion)
        db_context.session.add(user_data)
        db_context.session.commit()

    @staticmethod
    def update_user(user_data: User):
        user: User = UserRepository.get_user(user_data.identificacion)
        user.identificacion = user_data.identificacion or user.identificacion
        user.nombre = user_data.nombre or user.nombre
        user.apellido1 = user_data.apellido1 or user.apellido1
        user.apellido2 = user_data.apellido2 or user.apellido2
        user.correo = user_data.correo or user.correo
        user.id_perfil = user_data.id_perfil or user.id_perfil
        user.telefono = user_data.telefono or user.telefono
        db_context.session.commit()

    @staticmethod
    def get_user(identificacion: int):
        user: User = User.query.filter_by(identificacion=identificacion).first()
        if not user:
            raise NotFound('user doesn\'t exist')
        return user

    @staticmethod
    def get_user_by_id_or_email(identificacion: int, correo: str):
        user: User = User.query.filter(or_(User.identificacion==identificacion, User.correo==correo)).first()
        if not user:
            raise NotFound('user doesn\'t exist')
        return user

    @staticmethod
    def get_user_data(identificacion: int):
        query = text('select u.identificacion, u.nombre, u.apellido1, u.apellido2, u.correo, u.telefono, p.descripcion as perfil, u.id_perfil from ppi.usuario u, ppi.perfil p where u.id_perfil = p.id_perfil and u.identificacion = :identificacion')
        result_set = db_context.engine.execute(query, identificacion= identificacion)
        if result_set.rowcount == 0:
            raise NotFound('user doesn\'t exist')
        user_row = result_set.first()
        user = Utils.row2dict(user_row)
        return user

    @staticmethod
    def get_users():
        query = text('select u.identificacion, u.nombre, u.apellido1, u.apellido2, u.correo, u.telefono, p.descripcion as perfil, u.id_perfil from ppi.usuario u, ppi.perfil p where u.id_perfil = p.id_perfil')
        result = db_context.engine.execute(query)
        return [Utils.row2dict(user) for user in result]

    @staticmethod
    def delete_user(identificacion: int):
        pass