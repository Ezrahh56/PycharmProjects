print('*** Operador and ***')
# Regresa verdadero si ambos valores a evaluar son verdaderos
condicion1 = False
condicion2 = True
resultado = condicion1 and condicion2
print(f'El resultado {condicion1} and {condicion2}: es {resultado}')

print('*** Operador or ***')
# Regresa falso si ambos valores a evaluar son falsos

condicion1 = False
condicion2 = False
resultado = condicion1 or condicion2
print(f'El resultado {condicion1} or {condicion2} es: {resultado}')

print('*** Operador not ***')
condicion1 = False
resultado = not condicion1
print(f'Operador not sobre {condicion1}: {resultado}')

# Revisar si una variable es cadena vacía
nombre = ''
es_cadena_vacia = not nombre
print(f'\nLa variable no tiene ningún valor? {es_cadena_vacia}')

#Revisar si una variable no tiene ningún valor asignado
variable = None
es_variable_sin_valor = not variable
print(f'La variable no tiene ningún valor? {es_variable_sin_valor}')
