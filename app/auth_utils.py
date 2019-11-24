from flask_bcrypt import generate_password_hash, check_password_hash

class AuthUtils:

    @staticmethod
    def hash_password(password: str):
        return generate_password_hash(password.lower()).decode('utf-8')
    
    @staticmethod
    def compare_password(password_hash: str, password: str):
        print({'password': password, 'password_hash': password_hash})
        return check_password_hash(password_hash, password.lower())