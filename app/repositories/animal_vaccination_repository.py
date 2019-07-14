

class animalVaccinationRepository:

    __animalVaccination = []

    @staticmethod
    def create_animalVaccination(animalVaccination_data : VACUNAS_ANIMALES):
        db_context.session.add(animalVaccination_data)
        db_context.session.commit()
        
     @staticmethod
    def update_animalVaccination(animalVaccination_data: VACUNAS_ANIMALES):
        animalVaccination: VACUNAS_ANIMALES = VACUNAS_ANIMALES.query.filter_by(identificacion_animal
        = animalVaccination_data.identificacion_animal).first()
        if not animalVaccination:
            raise Exception('Vaccination doesn\'t exist')
            animalVaccination.identificacion_animal =  animalVaccination_data.identificacion_animal
            animalVaccination.id_vacuna =  animalVaccination_data.id_vacuna
            animalVaccination.fecha_programada =  animalVaccination_data.fecha_programada
            animalVaccination.evento =  animalVaccination_data.evento
            animalVaccination.fecha_ejecucion =  animalVaccination_data.fecha_ejecucion
            animalVaccination.id_via_aplicacion =  animalVaccination_data.id_via_aplicacion
            animalVaccination.dosis =  animalVaccination_data.dosis
            animalVaccination.id_laboratorio =  animalVaccination_data.id_laboratorio
            animalVaccination.reg_ica =  animalVaccination_data.reg_ica
            animalVaccination.nro_lote =  animalVaccination_data.nro_lote
            animalVaccination.tiempo_retiro =  animalVaccination_data.tiempo_retiro
            animalVaccination.observaciones =  animalVaccination_data.observaciones
        db_context.session.commit()
