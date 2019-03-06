from app.repositories import UserRepository

class AuthService:

    @staticmethod
    def create_user(name):
        user_data = {"name": name}
        UserRepository.create_user(user_data)

    @staticmethod
    def get_users():
        return UserRepository.get_users()