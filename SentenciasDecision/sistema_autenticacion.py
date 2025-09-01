print('*** Sistema de Autenticación ***')

USUARIO = 'Piero Pariona'
CONTRASENA = 123456
usuario = input('Colocar el usuario: ')
contrasena = int(input('Colocar la contraseña: '))

if usuario == USUARIO and contrasena == CONTRASENA:
    print('Bienvenido al Sistema')
elif usuario == USUARIO:
    print('Brindar nuevamente la contraseña ')
elif contrasena == CONTRASENA:
    print('Brindar nuevamente el usuario ')
else:
    print('Usuario y contraseña incorrectos ')