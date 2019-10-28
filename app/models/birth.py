from app.repositories import db_context

class Birth(db_context.Model):

    __tablename__ = "PARTO"

    
    id_camada = db_context.Column(db_context.Integer, primary_key=True)
    identificacion_animal  = db_context.Column(db_context.Integer, db_context.ForeignKey('ANIMAL.identificacion_animal'), nullable=False) 
    fecha_monta = db_context.Column(db_context.Date, nullable=False)
    tipo_servicio = db_context.Column(db_context.String(100), nullable=False )
    identificacion_macho = db_context.Column(db_context.Integer, nullable=True)
    fecha_probable_parto = db_context.Column(db_context.Date, nullable=False)
    fecha_parto = db_context.Column(db_context.Date, nullable=False)
    jaula_parto = db_context.Column(db_context.String(100), nullable=False)
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
    jaula_destete = db_context.Column(db_context.String(100), nullable=False)
    animal = db_context.relationship('Animal', backref="PARTO", uselist=False, lazy='noload')


    @property
    def serialized(self):
        return {
            'id_camada': self.id_camada,
            'identificacion_animal': self.identificacion_animal,
            'fecha_monta': self.fecha_monta,
            'tipo_servicio': self.tipo_servicio,
            'identificacion_macho': self.identificacion_macho,
            'fecha_probable_parto': self.fecha_probable_parto,
            'fecha_parto': self.fecha_parto,
            'jaula_parto': self.jaula_parto,
            'numero_lechones_vivos_parto': self.numero_lechones_vivos_parto,
            'numero_lechones_muertos_parto': self.numero_lechones_muertos_parto,
            'numero_machos_parto': self.numero_machos_parto,
            'numero_hembras_parto': self.numero_hembras_parto,
            'numero_momias': self.numero_momias,
            'peso_total_vivos': self.peso_total_vivos,
            'fecha_probable_destete': self.fecha_probable_destete,
            'fecha_destete': self.fecha_destete,
            'numero_hembras_destete': self.numero_hembras_destete,
            'numero_machos_destete': self.numero_machos_destete,
            'numero_muertos_destete': self.numero_muertos_destete,
            'dias_lactancia': self.dias_lactancia,
            'peso_total_destete': self.peso_total_destete,
            'jaula_destete': self.jaula_destete,
            'animal': self.animal.serialized if self.animal else None
        }
