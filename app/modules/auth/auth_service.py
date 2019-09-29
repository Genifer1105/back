from app.models import User
from app.repositories import UserRepository
from app.utils import Utils

class AuthService:

    @staticmethod
    def create_user(user_data: dict):
        identificacion = Utils.validate_json_field(user_data, 'identificacion', int, True)
        nombre = Utils.validate_json_field(user_data, 'nombre', str, True)
        apellido1 = Utils.validate_json_field(user_data, 'apellido1', str, True)
        apellido2 = Utils.validate_json_field(user_data, 'apellido2', str, False)
        correo = Utils.validate_json_field(user_data, 'correo', str, True)
        contrasena = Utils.validate_json_field(user_data, 'contrasena', str, True)
        id_perfil = Utils.validate_json_field(user_data, 'id_perfil', int, True)
        telefono = Utils.validate_json_field(user_data, 'telefono', str, False)
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
        userCreated = UserRepository.get_user(identificacion) 
        return userCreated.serialize()

    @staticmethod
    def update_user(user_data, identificacion):
        identificacion = Utils.validate_field(identificacion, 'identificacion', int, False)
        nombre = Utils.validate_json_field(user_data, 'nombre', str, False)
        apellido1 = Utils.validate_json_field(user_data, 'apellido1', str, False)
        apellido2 = Utils.validate_json_field(user_data, 'apellido2', str, False)
        correo = Utils.validate_json_field(user_data, 'correo', str, False)
        contrasena = Utils.validate_json_field(user_data, 'contrasena', str, False)
        id_perfil = Utils.validate_json_field(user_data, 'id_perfil', int, False)
        telefono = Utils.validate_json_field(user_data, 'telefono', str, False)
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
        userUpdated = UserRepository.get_user(identificacion) 
        return userUpdated.serialize()

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