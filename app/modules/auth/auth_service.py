from app.models import User
from app.repositories import UserRepository
from app.utils import Utils
from app.auth_utils import AuthUtils
from werkzeug.exceptions import Conflict, NotFound, Unauthorized, InternalServerError
from flask_jwt_extended import create_access_token
from smtplib import SMTP
from datetime import datetime
from flask_jwt_extended import get_jwt_identity
import string

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
            correo = str.strip(correo).lower(),
            contrasena = AuthUtils.hash_password(contrasena),
            id_perfil = id_perfil,
            telefono = telefono if not telefono else str.strip(telefono)
        )
        print('user password', user.contrasena)
        UserRepository.create_user(user)
        userCreated = UserRepository.get_user(identificacion) 
        return userCreated.serialized

    @staticmethod
    def login(identificacion: int, correo: str, contrasena: str):
        password_checked = False
        user_data: User = None
        correo = correo.lower() if correo else None
        try:
            user_data = UserRepository.get_user_by_id_or_email(identificacion, correo)
            password_checked = AuthUtils.compare_password(user_data.contrasena, contrasena)
        except NotFound:
            pass
        if not password_checked:
            raise Unauthorized('Wrong user or password')
        token = create_access_token({ "identificacion": user_data.identificacion, "profile": user_data.id_perfil })
        return user_data.serialized, token


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
            correo = str.strip(correo).lower() if correo else None,
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
        

    @staticmethod
    def change_password(identificacion: int, password: str, new_password: str):
        user_data = UserRepository.get_user_by_id_or_email(identificacion, None)
        password_checked = AuthUtils.compare_password(user_data.contrasena, password)
        if not password_checked:
            raise Unauthorized('wrong password')
        new_password_hash = AuthUtils.hash_password(new_password)
        user_data.contrasena = new_password_hash
        UserRepository.update_user(user_data)

    
    @staticmethod
    def password_recover(email: str):
        user_data = UserRepository.get_user_by_id_or_email(None, email)
        if not user_data:
            raise NotFound('user not found')
        full_name = f'{user_data.nombre} {user_data.apellido1}'
        new_password = Utils.get_random_string(10)
        new_password_hash = AuthUtils.hash_password(new_password)
        user_data.contrasena = new_password_hash
        UserRepository.update_user(user_data)
        message_data = f'Hola {full_name}, hemos recibido tu solicitud de recuperación de cuenta.\n\n'+\
            f'Tu nueva contraseña es: {new_password}\n\n'+\
            'Recuerda cambiarla en cuanto puedas'
        # try:
        smtp_instance = SMTP('smtp.gmail.com', 587)
        smtp_instance.starttls()
        smtp_instance.login('porcipoli@gmail.com', 'ppi12345')
        message = f'Subject: Account Recover\n\n{message_data}'.encode('utf-8')
        smtp_instance.sendmail('porcipoli@gmail.com', email, message)
        smtp_instance.quit()
        # except Exception as ex:
        #     print(ex)
        #     raise InternalServerError