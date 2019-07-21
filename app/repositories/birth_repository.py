







class BirthRepository:

    __births = []

    @staticmethod
    def create_cagesLitter(birth_data : PARTOS):
        db_context.session.add(birth_data)
        db_context.session.commit()

    @staticmethod
    def update_user(birth_data: PARTOS):
        birth: PARTOS = PARTOS.query.filter_by(id_jaula_parto=cagesBirths_data.id_jaula_parto).first()
        if not birth:
            raise Exception('Birth birth doesn\'t exist')
        birth.identificacion_animal = birth_data.identificacion_animal
        birth.fecha_monta = birth_data.fecha_monta
        birth.id_tipo_servicio = birth_data.id_tipo_servicio
        birth.identificacion_macho = birth_data.identificacion_macho
        birth.fecha_probable_parto = birth_data.fecha_probable_parto
        birth.id_camada = birth_data.id_camada
        birth.fecha_parto = birth_data.fecha_parto
        birth.id_jaula_parto = birth_data.id_jaula_parto
        birth.numeros_lechones_vivos_parto = birth_data.numeros_lechones_vivos_parto
        birth.numero_lechones_muertos_parto = birth_data.numero_lechones_muertos_parto
        birth.numero_machos_parto = birth_data.numero_machos_parto
        birth.numero_hembras_parto = birth_data.numero_hembras_parto
        birth.numero_momias = birth_data.numero_momias
        birth.peso_total_vivos = birth_data.peso_total_vivos
        birth.fecha_probable_destete = birth_data.fecha_probable_destete
        birth.fecha_destete = birth_data.fecha_destete
        birth.numero_hembras_destete = birth_data.numero_hembras_destete
        birth.numero_machos_destete = birth_data.numero_machos_destete
        birth.numero_muertos_destete = birth_data.numero_muertos_destete
        birth.dias_lactancia = birth_data.dias_lactancia
        birth.peso_total_destete = birth_data.peso_total_destete
        birth.id_jaula_destete = birth_data.id_jaula_destete
       
        db_context.session.commit()