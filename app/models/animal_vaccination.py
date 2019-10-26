from app.repositories import db_context
class AnimalVaccination(db_context.Model):

    __tablename__ = "VACUNAS_ANIMALES"

    identificacion_animal  = db_context.Column(db_context.Integer, db_context.ForeignKey('ANIMALES.id_vacuna'), primary_key=True) 
    id_vacuna = db_context.Column(db_context.Integer, db_context.ForeignKey('VACUNAS.id_vacuna'), primary_key=True) 
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
    vacuna = db_context.relationship('Vaccine', backref="VACUNAS_ANIMALES", uselist=False, lazy='noload')
    animal = db_context.relationship('Animal', backref="VACUNAS_ANIMALES", uselist=False, lazy='noload')

    @property
    def serialized(self):
        return {
            'identificacion_animal': self.identificacion_animal,
            'id_vacuna': self.id_vacuna,
            'fecha_programada': self.fecha_programada,
            'evento': self.evento,
            'fecha_ejecucion': self.fecha_ejecucion,
            'id_via_aplicacion': self.id_via_aplicacion,
            'dosis': self.dosis,
            'id_laboratorio': self.id_laboratorio,
            'reg_ica': self.reg_ica,
            'nro_lote': self.nro_lote,
            'tiempo_retiro': self.tiempo_retiro,
            'observaciones': self.observaciones,
            'vacuna': self.vacuna.serialized if self.vacuna else None,
            'animal': self.animal.serialized if self.animal else None
        }




