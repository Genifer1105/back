from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
db_context = SQLAlchemy()
Base = declarative_base()
