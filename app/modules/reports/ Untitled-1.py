data = [
    {'id_camada': 123, 'identificacion_animal': 123, 'total': 30}, 
    {'id_camada': 4, 'identificacion_animal': 1235, 'total': 0}, 
    {'id_camada': 1020, 'identificacion_animal': 1235, 'total': 15}
]


result_data = []
current_animal_data = None
current_animal_id = None
key_id_animal = 'identificacion_animal'
key_births = 'births'
key_total = 'total'
index = 0

for birth_data in data:
    identificacion_animal = birth_data[key_id_animal]
    if identificacion_animal != current_animal_id:
        current_animal_id = identificacion_animal
        current_animal_data = {
            key_id_animal: identificacion_animal,
            key_births: [],
            key_total: 0
        }
        result_data.append(current_animal_data)
    current_animal_data[key_births].append(birth_data)
    current_animal_data[key_total] += birth_data[key_total]
[
    {
        'identificacion_animal': 123, 
        'births': [
            {'id_camada': 123, 'identificacion_animal': 123, 'total': 30}
        ], 
        'total': 30
    },
    {
        'identificacion_animal': 1235,
        'births': [
            {'id_camada': 4, 'identificacion_animal': 1235, 'total': 0},
            {'id_camada': 1020, 'identificacion_animal': 1235, 'total': 15}
        ], 
        'total': 15
    }
]
print(result_data)