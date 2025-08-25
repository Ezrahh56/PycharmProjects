
print('*** Sistema Generador de Emails***')
nombre = input('Cuáles son sus nombres: ')
apellido = input('Cuáles son sus apellidos: ')
empresa = input('Nombre de la empresa: ')
ex_dom = input('Colocar la extensión de dominio: ')
nom = nombre.strip().lower().replace(' ','.')
apell = '.' + apellido.strip().lower().replace(' ','.')
empr = '@' + empresa.strip().lower().replace(' ','')
email = f'{nom}{apell}{empr}{ex_dom}'
print(f'''
Su nuevo correo es: 
    {email}
    Felicidades''')