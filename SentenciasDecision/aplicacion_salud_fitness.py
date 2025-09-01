print('*** Aplicación de Salud y Fitness ***')

# Constantes
META_PASOS_DIARIO = 10000
CALORIAS_POR_PASO = 0.04 # Valor aproximado, son kilocalorías

# Pedimos los valores al usuario
nombre_usuario = input('Cuál es tu nombre? ')
pasos_diarios = int(input('Cuántos pasos has caminado hoy? '))

# Verifica si el usuario alcanzó la meta de pasos diarios
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIO
meta_alcanzada_txt = 'Si' if meta_alcanzada else 'No'
# Calculamos las calorias quemadas
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

# Mostramos la información
print(f'\nUsuario: {nombre_usuario}')
print(f'Pasos dados: {pasos_diarios}')
print(f'Calorias quemadas: {calorias_quemadas} kcal')
print(f'Meta de pasos diario alcanzada: {meta_alcanzada_txt}')
print(f'La meta de pasos diario es de: {META_PASOS_DIARIO} pasos')