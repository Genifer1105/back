from datetime import timedelta

class Configuration():
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:chuck norris@localhost/ppi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = '08F795D0AE8EDA93F76B2943F2825014A31A6601F352966772C71416912B8CA7'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
