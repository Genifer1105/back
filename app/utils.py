from werkzeug.exceptions import BadRequest
from datetime import datetime

class Utils:

    @staticmethod
    def validate_json_field(json: dict, field_key: str, required: bool, field_type: type):
        field = json.get(field_key, None)
        return Utils.validate_field(field, field_key, field_type, required)
    
    @staticmethod
    def validate_field(field, field_key: str, field_type: type, required: bool):
        if field is None:
            if required:
                raise BadRequest(f"field { field_key } is required")
        elif not isinstance(field, field_type):
            raise BadRequest(f"field { field_key } must be { Utils._get_type_as_str(field_type) }")
        return field
    
    @staticmethod
    def convert_to_date(date_str: str, date_format: str):
        try:
            return datetime.strptime(date_str, date_format).date()
        except ValueError:
            raise BadRequest("field doesn't match the format")

    @staticmethod
    def _get_type_as_str(field_type: type):
        if field_type == str:
            return 'string'
        elif field_type == int:
            return 'integer'
        elif field_type == float:
            return 'float'
        elif field_type == bool:
            return 'boolean'