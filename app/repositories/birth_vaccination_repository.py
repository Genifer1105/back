

class BirthVaccinationRepository:

    __birthVaccination = []

 @staticmethod
    def create_birthVaccination(birthVaccination_data : VACUNAS_CAMADAS):
        db_context.session.add(birthVaccination_data)
        db_context.session.commit()

     @staticmethod
    def update_birthVaccination(birthVaccination_data: VACUNAS_CAMADAS):
        birthVaccination: VACUNAS_CAMADAS  = VACUNAS_CAMADAS.query.filter_by(identificacion_camada
        =user_data.identificacion_camada).first()
        if not birthVaccination:
            raise Exception('Vaccination doesn\'t exist')
            birthVaccination.identificacion_camada = birthVaccination_data.identificacion_camada
            birthVaccination.id_vacuna = birthVaccination_data.id_vacuna
            birthVaccination.fecha_programada = birthVaccination_data.fecha_programada
            birthVaccination.evento = birthVaccination_data.evento
            birthVaccination.fecha_ejecucion = birthVaccination_data.fecha_ejecucion
            birthVaccination.id_via_aplicacion = birthVaccination_data.id_via_aplicacion
            birthVaccination.dosis = birthVaccination_data.dosis
            birthVaccination.id_laboratorio = birthVaccination_data.id_laboratorio
            birthVaccination.reg_ica = birthVaccination_data.reg_ica
            birthVaccination.nro_lote = birthVaccination_data.nro_lote
            birthVaccination.tiempo_retiro = birthVaccination_data.tiempo_retiro
            birthVaccination.observaciones = birthVaccination_data.observaciones  
        db_context.session.commit()