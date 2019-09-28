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
        if (not AuthService.__validate_user_data_update(identificacion, nombre, apellido1, apellido2, correo, contrasena, id_perfil, telefono)):
                raise Exception('invalid arguments')
        user = User(
            identificacion = identificacion,
            nombre = str.strip(nombre) if nombre else None,
            apellido1 = str.strip(apellido1) if apellido1 else None,
            apellido2 = str.strip(apellido2) if apellido2 else None,
            correo = str.strip(correo) if correo else None,
            contrasena = contrasena,
            id_perfil = id_perfil,
            telefono = str.strip(telefono) if telefono else None
        )
        UserRepository.update_user(user)

    @staticmethod
    def get_users():
        return UserRepository.get_users()


    @staticmethod
    def __validate_user_data(identificacion, nombre, apellido1, apellido2, correo, contrasena, id_perfil, telefono) -> bool:
        return (
            isinstance(identificacion, int) 
            and isinstance(nombre, str)
            and isinstance(apellido1, str)
            and (apellido2 is None or isinstance(apellido2, str))
            and isinstance(correo, str)
            and isinstance(contrasena, str)
            and isinstance(id_perfil, int)
            and (telefono is None or isinstance(telefono, str))
        )

    @staticmethod
    def __validate_user_data_update(identificacion, nombre, apellido1, apellido2, correo, contrasena, id_perfil, telefono) -> bool:
        return (
            (identificacion is None or isinstance(identificacion, int))
            and (nombre is None or isinstance(nombre, str))
            and (apellido1 is None or isinstance(apellido1, str))
            and (apellido2 is None or isinstance(apellido2, str))
            and (correo is None or isinstance(correo, str))
            and (contrasena is None or isinstance(contrasena, str))
            and (id_perfil is None or isinstance(id_perfil, int))
            and (telefono is None or isinstance(telefono, str))
        )