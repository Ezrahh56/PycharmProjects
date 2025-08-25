# Conversion de tipos de datos

# Convertir de cadena a numero
numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'Valor numérico en cadena: {numero_cadena}')
print(f'Cadena a entero: {numero_entero}')

#Convertir de cadena a flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print(f'Cadena a flotante: {numero_flotante}')

# Convertir de numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Número a cadena: {numero_cadena}')

# Convertir a booleano
#Tipo de bool es False en los siguiente casos
# Si el valor es 0, cadena vacía o None entonces regresa False
# Regresa True si el valor es distinto de 0 si es distintio de cadena vacía
# y tambien si es distinto de None
numero_entero = 0
booleano = bool(numero_entero)
print(f'Valor booleano de 0: {booleano}') # False, incluye 0, 0.0

numero_entero = 5
booleano = bool(numero_entero)
print(f'Valor booleano de 5: {booleano}') #True

cadena = '' # El larfo de la cadena es 0
booleano = bool(cadena)
print(f'valor booleano de cadena vacia: {booleano}') # False, incluye colecciones vacias

cadena = 'Cadena con valor'
booleano = bool(cadena)
print(f'Valor booleano de cadena no vacia: {booleano}') #True

variable = None
booleano = bool(variable)
print(f'Valor booleano de None: {booleano}') #False