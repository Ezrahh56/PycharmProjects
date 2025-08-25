print('*** Sistema Generador de ID Único ***')
nombre = input('Cuál es tu nombre: ')
apellido = input('Cuál es tu apellido: ')
nacimiento = input('Cuál es tu año de nacimiento (YYYY): ')
nom = nombre[0:2].upper().strip()
apell = apellido[0:2].upper().strip()
naci = nacimiento.strip()[2:4] # tambien se puede hacer solo usando lo de la izquierda
from random import randint
cifras = str(randint(1000,9999))
id = nom + apell + naci + cifras
#id = f'{nom}{apell}{naci}{cifras}' esta seria la forma correcta de hacerlo
print(f'\nHola {nombre},')
print(f'\tTu nuevo número de identificación (ID) generado por el sistema es:\n\t{id}\n\tFelicidades¡')