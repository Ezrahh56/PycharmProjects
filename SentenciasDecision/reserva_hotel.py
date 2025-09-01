print('*** Sistem Reserva Hotel ***')

nombre = input('Nombre de Cliente: ')
dias = int(input('Días de estadía: '))
vista = input('Con vista al mar(si/no)? ')
vista1 = vista.strip().lower()
vista2 = vista1 == 'si'
precio = dias * 190.50 if vista2 else dias * 150.50
print(f'\n---------------Detalles de la Reservación------------')
print(f'Cliente: {nombre}')
print(f'Días de estadía: {dias}')
print(f'Costo total: ${precio:.2f}')
print(f'Habitación con vista al mar: {vista}')

