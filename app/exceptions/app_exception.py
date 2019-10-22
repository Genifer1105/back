from werkzeug.exceptions import HTTPException
from flask import jsonify

class AppException(HTTPException):
    
    @staticmethod
    def error_handler(error):
        response = jsonify(message=error.description)
        response.status_code = error.code if isinstance(error, HTTPException) else 500
        return response