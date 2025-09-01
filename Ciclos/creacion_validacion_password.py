print('*** Creación y Validación de Password ***')

contrasena = True
while contrasena:
    print('''Validación de contraseñas''')
    contra = input('Escribe tu contraseña: ')
    if len(contra) == 6:
        print('Password Válido\n')
    else:
        print('Password Inválido\n')