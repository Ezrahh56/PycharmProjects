print('*** Valor dentro de Rango ***')

MINIMO = 0
MAXIMO = 5

valor = int(input('Escribe un valor dentro de 0 y 5: '))

valor_final = MINIMO <= valor <= MAXIMO

print(f'Valor dentro del rango: {valor_final}')