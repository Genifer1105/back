from functools import wraps
from app.repositories import UserRepository
from app.models import User
from werkzeug.exceptions import Unauthorized, NotFound
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

def authorize(profile=None):
    def authorize_decorator(fn):
        print('(decorator)'*50)
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            data = get_jwt_identity()
            print('token data: ' + str(data))
            try:
                UserRepository.get_user(data.get('identificacion'))
            except NotFound:
                raise Unauthorized('User not found')
            print({'data': data, 'profile': profile})
            if profile is not None and data.get('profile') != profile:
                raise Unauthorized('profile doesn\'t match')
            return fn(*args, **kwargs)
        return wrapper
    return authorize_decorator