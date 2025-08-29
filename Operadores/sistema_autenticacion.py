print('*** Sistema Autenticación ***')

usuario_correcto = 'Piero'
contrasena_correcta = 123456

usuario = str(input('Proporciona tu usuario: '))
contrasena = int(input('Proporciona tu contraseña: '))

correcto = (usuario == usuario_correcto and contrasena == contrasena_correcta)
print(f"Datos correctos? {correcto}")
