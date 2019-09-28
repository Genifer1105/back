from app.repositories import db_context

class Births(db_context.Model):

    __tablename__ = "PARTOS"


    identificion_animal = db_context.Column(db_context.Integer, nullable=False )
    fecha_monta = db_context.Column(db_context.Date, nullable=False)
    id_tipo_servicio = db_context.Column(db_context.Integer, nullable=False )
    identificacion_macho = db_context.Column(db_context.Integer, nullable=True)
    fecha_probable_parto = db_context.Column(db_context.Date, nullable=False)
    id_camada = db_context.Column(db_context.Integer, primary_key=True)
    fecha_parto = db_context.Column(db_context.Date, nullable=False)
    id_jaula_parto = db_context.Column(db_context.Integer, nullable=False)
    numero_lechones_vivos_parto = db_context.Column(db_context.Integer, nullable=False)
    numero_lechones_muertos_parto = db_context.Column(db_context.Integer, nullable=False)
    numero_machos_parto = db_context.Column(db_context.Integer, nullable=False)
    numero_hembras_parto = db_context.Column(db_context.Integer, nullable=False)
    numero_momias = db_context.Column(db_context.Integer, nullable=False)
    peso_total_vivos = db_context.Column(db_context.Integer, nullable=False )
    fecha_probable_destete = db_context.Column(db_context.Date, nullable=True )
    fecha_destete = db_context.Column(db_context.Date, nullable=True)
    numero_hembras_destete = db_context.Column(db_context.Integer, nullable=True)
    numero_machos_destete = db_context.Column(db_context.Integer, nullable=True)
    numero_muertos_destete = db_context.Column(db_context.Integer, nullable=True)
    dias_lactancia = db_context.Column(db_context.Integer, nullable=False )
    peso_total_destete = db_context.Column(db_context.Integer, nullable=False)
    id_jaula_destete = db_context.Column(db_context.Integer, nullable=False)



