
# personajes = ['Harry', 'Hermione', 'Ron', 'Draco']
# casas = ['Gryffindor', 'Slytherin']


# dicx1 = {
#     'name': 'Harry',
#     'casa': 'Gryffindor',
#     'patronus': 'Ciervo'
# }
# dicx2 = {
#     'name': 'Hermione',
#     'casa': 'Gryffindor',
#     'patronus': 'Nutria'
# }
# dicx3 = {
#     'name': 'Ron',
#     'casa': 'Gryffindor',
#     'patronus': 'Jack Russell Terrier'
# }


personajes = [
    {'name': 'Harry','casa': 'Gryffindor','patronus': 'Ciervo'},
    {'name': 'Hermione','casa': 'Gryffindor','patronus': 'Nutria'},
    {'name': 'Ron','casa': 'Gryffindor','patronus': 'Jack Russell Terrier'}

]

# 1. Cual es el patronus de Harry
# print(dicx1['patronus'])

for personaje in personajes:
    if personaje['name'] == 'Harry':
        print(personaje['patronus'])
        
