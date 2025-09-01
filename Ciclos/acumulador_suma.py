from xmlrpc.server import MultiPathXMLRPCServer

print('*** Suma Acumulativa ****')

MAXIMO = 5
numero = 1
acumulador_suma = 0
while numero <= MAXIMO:
    # Imprimir lo que se va a sumar
    print(f'Acumulador_suma + numero -> {acumulador_suma} + {numero}')
    acumulador_suma += numero
    numero += 1
    # Imprimir el resultado de la suma parcial
    print(f'Suma parcial acumulada: {acumulador_suma}\n')
print(f'\nResultados suma acumulada: {acumulador_suma}')