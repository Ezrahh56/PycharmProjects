print('*** Sistema de Empleados ***')
nombre_empleado = input('Nombre del empleado: ')
edad_empleado = int(input('Edad del empleado: '))
salario_empleado = float(input('Salario del empleado: '))
es_jefe_departamento = input('Es jefe departamento (Si/No)?')

#Vamos a cconvertir a un tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == 'si'
# Gracias a la comparativa si es si entonces dará True sino False
print(f'\nDatos del Empleado')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado:.2f}') #con esto determinamos los decimales y que es tipo flotante
print(f'Es jefe de Departamento?: {es_jefe_departamento}')
