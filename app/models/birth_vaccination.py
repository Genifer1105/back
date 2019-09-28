
from app.repositories import db_context

class BirthVaccination(db_context.Model):

    __tablename__ = "VACUNAS_CAMADAS"


    identificacion_camada  = db_context.Column(db_context.Integer, primary_key=True) 
    id_vacuna = db_context.Column(db_context.Integer, primary_key=True) 
    fecha_programada = db_context.Column(db_context.Date, primary_key=True)  
    evento = db_context.Column(db_context.String(100), nullable=False)  
    fecha_ejecucion = db_context.Column(db_context.Date, nullable=True)  
    id_via_aplicacion = db_context.Column(db_context.Integer, nullable=False) 
    dosis = db_context.Column(db_context.Integer, nullable=False) 
    id_laboratorio = db_context.Column(db_context.Integer, nullable=False) 
    reg_ica = db_context.Column(db_context.String(100), nullable=False)
    nro_lote = db_context.Column(db_context.String(100), nullable=False)  
    tiempo_retiro = db_context.Column(db_context.String(100), nullable=True)
    observaciones = db_context.Column(db_context.String(200), nullable=True)  
