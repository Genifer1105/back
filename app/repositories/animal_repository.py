

class animalRepository:

    __animal = []

 @staticmethod
    def create_animal(animal_data : ANIMALES):
        db_context.session.add(animal_data)
        db_context.session.commit()

    @staticmethod
    def update_animal(animal_data: ANIMALES):
        animal: ANIMALES = ANIMALES.query.filter_by(identificacion_animal = animal_data.ntificacion_animal).first()
        if not usanimaler:
            raise Exception('Animal doesn\'t exist')
            animal.identificacion_animal = animal_data.identificacion_animal
            animal.id_raza = animal_data.id_raza
            animal.fecha_nacimiento = animal_data.fecha_nacimiento
            animal.id_madre = animal_data.id_madre
            animal.id_padre = animal_data.id_padre
            animal.procedencia = animal_data.procedencia
            db_context.session.commit()

        