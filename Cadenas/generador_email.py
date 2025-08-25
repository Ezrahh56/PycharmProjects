print('*** Generador de Email***')
nombre = ' Ubaldo Acosta Soto '
nombre1 = nombre.strip() #Esto sirve para quitar los espacios de los lados
print(f'Nombre usuario: {nombre1}')
nombrenew = nombre1.lower().replace(' ','.') #con lower lo puse en minusculas y replace para reemplazar texto
print(f'Nombre usuario normalizado: {nombrenew}')
empresa = ' Global Mentoring '
empresa1 = empresa.strip()
print(f'\nNombre empresa: {empresa1}') #Esto es para hacer el salto de linea
dominio = ' .com.mx '
dominio1 = dominio.strip()
print(f'Extensión del dominio: {dominio1}')
email = '@' + empresa1.replace(' Mentoring','Mentoring') + dominio1 #Aca igualmente reemplace una parte del texto
                                                                    #porque no sé como sacar el espacio del medio
print(f'Dominio de email normalizado: {email.lower()}') #aca en minusculas
email_generado = nombrenew + email.lower() #aca se concatenatodo lo que hay
print()
print(f'Email final generado: {email_generado}')

