from app.models import User
from app.repositories import UserRepository
from app.utils import Utils
from app.auth_utils import AuthUtils
from werkzeug.exceptions import Conflict, NotFound, Unauthorized

class AuthService:

    @staticmethod
    def create_user(identificacion: int, nombre: str, apellido1: str, apellido2: str, correo: str, contrasena: str, id_perfil: int, telefono: str):
        try:
            UserRepository.get_user_data(identificacion)
        except NotFound:
            pass
        user = User(
            identificacion = identificacion,
            nombre = str.strip(nombre),
            apellido1 = str.strip(apellido1),
            apellido2 = apellido2 if not apellido2 else str.strip(apellido2),
            correo = str.strip(correo),
            contrasena = AuthUtils.hash_password(contrasena),
            id_perfil = id_perfil,
            telefono = telefono if not telefono else str.strip(telefono)
        )
        print('user password', user.contrasena)
        UserRepository.create_user(user)
        userCreated = UserRepository.get_user(identificacion) 
        return userCreated.serialized

    @staticmethod
    def login(identificacion: int, contrasena: str):
        password_checked = False
        user_data: User = None
        try:
            user_data = UserRepository.get_user(identificacion)
            password_checked = AuthUtils.compare_password(user_data.contrasena, contrasena)
        except NotFound:
            pass
        if not password_checked:
            raise Unauthorized('Wrong user or password')
        return user_data.serialized


    @staticmethod
    def update_user(identificacion: int, nombre: str, apellido1: str, apellido2: str, correo: str, id_perfil: int, telefono: str):
        try:
            UserRepository.get_user_data(identificacion)
        except NotFound:
            pass
        user = User(
            identificacion = identificacion,
            nombre = str.strip(nombre) if nombre else None,
            apellido1 = str.strip(apellido1) if apellido1 else None,
            apellido2 = str.strip(apellido2) if apellido2 else None,
            correo = str.strip(correo) if correo else None,
            id_perfil = id_perfil,
            telefono = str.strip(telefono) if telefono else None
        )
        UserRepository.update_user(user)
        userUpdated = UserRepository.get_user(identificacion) 
        return userUpdated.serialized

    @staticmethod
    def get_users():
        return UserRepository.get_users()

    @staticmethod
    def get_user(identificacion):
        return UserRepository.get_user_data(identificacion)