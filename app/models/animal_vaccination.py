from app.repositories import db_context
class AnimalVaccination(db_context.Model):

    __tablename__ = "PLAN_VACUNACIONAL_ANIMAL"

    identificacion_animal  = db_context.Column(db_context.Integer, db_context.ForeignKey('ANIMAL.identificacion_animal'), primary_key=True) 
    vacuna = db_context.Column(db_context.String(100), primary_key=True) 
    fecha_programada = db_context.Column(db_context.Date, primary_key=True)  
    evento = db_context.Column(db_context.String(100), nullable=False)  
    fecha_ejecucion = db_context.Column(db_context.Date, nullable=True)  
    via_aplicacion = db_context.Column(db_context.String(100), nullable=False) 
    dosis = db_context.Column(db_context.Integer, nullable=False) 
    laboratorio = db_context.Column(db_context.String(100), nullable=False) 
    reg_ica = db_context.Column(db_context.String(100), nullable=False)
    nro_lote = db_context.Column(db_context.String(100), nullable=False)  
    tiempo_retiro = db_context.Column(db_context.String(100), nullable=True)
    observaciones = db_context.Column(db_context.String(200), nullable=True)
    animal = db_context.relationship('Animal', backref="PLAN_VACUNACIONAL_ANIMAL", uselist=False, lazy='noload')

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
            'animal': self.animal.serialized if self.animal else None,
            'vacuna': self.vacuna,
            'laboratorio': self.laboratorio,
            'via_aplicacion': self.via_aplicacion
        }




