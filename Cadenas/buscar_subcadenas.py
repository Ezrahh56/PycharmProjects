# Buscar subcadenas

cadena = 'Hola, mundo?'
indice = cadena.find('mundo') # solo trae el indice de la primera coincidencia de la primer subcadena
print(f'Indice de la subcadena mundo: {indice}')

# Obtener el indice de la subcadena de Hola
indice = cadena.find('Hola')
print(f'Indice de la subcadena de Hola: {indice}')