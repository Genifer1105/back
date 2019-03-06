class UserRepository:

    __users = []

    @staticmethod
    def create_user(user):
        UserRepository.__users.append(user)

    @staticmethod
    def get_users():
        return UserRepository.__users