from app.models import User
from app.repositories import UserRepository

class AuthService:

    @staticmethod
    def create_user(user_data: dict):
        identificacion = user_data.get('identificacion')
        nombre = user_data.get('nombre')
        apellido1 = user_data.get('apellido1')
        apellido2 = user_data.get('apellido2')
        correo = user_data.get('correo')
        contrasena = user_data.get('contrasena')
        id_perfil = user_data.get('id_perfil')
        telefono = user_data.get('telefono')
        if (not AuthService.__validate_user_data(identificacion, nombre, apellido1, apellido2, correo, contrasena, id_perfil, telefono)):
                raise Exception('invalid arguments')
        user = User(
            identificacion = identificacion,
            nombre = str.strip(nombre),
            apellido1 = str.strip(apellido1),
            apellido2 = apellido2 if not apellido2 else str.strip(apellido2),
            correo = str.strip(correo),
            contrasena = contrasena,
            id_perfil = id_perfil,
            telefono = telefono if not telefono else str.strip(telefono)
        )
        UserRepository.create_user(user)

    @staticmethod
    def update_user(user_data):
        identificacion = user_data.get('identificacion')
        nombre = user_data.get('nombre')
        apellido1 = user_data.get('apellido1')
        apellido2 = user_data.get('apellido2')
        correo = user_data.get('correo')
        contrasena = user_data.get('contrasena')
        id_perfil = user_data.get('id_perfil')
        telefono = user_data.get('telefono')
        if (not AuthService.__validate_user_data(identificacion, nombre, apellido1, apellido2, correo, contrasena, id_perfil, telefono)):
                raise Exception('invalid arguments')
        user = User(
            identificacion = identificacion,
            nombre = str.strip(nombre),
            apellido1 = str.strip(apellido1),
            apellido2 = apellido2 if not apellido2 else str.strip(apellido2),
            correo = str.strip(correo),
            contrasena = contrasena,
            id_perfil = id_perfil,
            telefono = telefono if not telefono else str.strip(telefono)
        )
        UserRepository.update_user(user)

    @staticmethod
    def get_users():
        return UserRepository.get_users()


    @staticmethod
    def __validate_user_data(identificacion, nombre, apellido1, apellido2, correo, contrasena, id_perfil, telefono) -> bool:
        return (
            isinstance(identificacion, int) 
            or isinstance(nombre, str)
            or isinstance(apellido1, str)
            or (not apellido2 or isinstance(apellido2, str))
            or isinstance(correo, str)
            or isinstance(contrasena, str)
            or isinstance(id_perfil, int)
            or (not telefono or isinstance(telefono, str))
        )