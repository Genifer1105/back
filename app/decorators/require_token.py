from functools import wraps
from app.repositories import UserRepository
from app.models import User
from werkzeug.exceptions import Unauthorized, NotFound
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, verify_jwt_in_request_optional

def authorize(profiles=[1, 2]):
    def authorize_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            verify_jwt_in_request_optional()
            data = get_jwt_identity()
            print('token data: ' + str(data))
            try:
                UserRepository.get_user(data.get('identificacion'))
            except NotFound:
                raise Unauthorized('User not found')
            print({'data': data, 'profile': profiles})
            if profiles is not None and data.get('profile') not in profiles:
                raise Unauthorized('profile doesn\'t match')
            return fn(*args, **kwargs)
        return wrapper
    return authorize_decorator