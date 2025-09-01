print('*** Sistemad de envíos ***')

tarifa = input('Seleccionar tarifa Nacional o Internacional: ')
peso = float(input('Peso del paquete en Kg: '))
tarifa1 = tarifa.strip().lower()
valor = peso * 10 if tarifa1 == 'nacional' else peso * 20
print(f'El costo total del envío es ${valor:.2f}')