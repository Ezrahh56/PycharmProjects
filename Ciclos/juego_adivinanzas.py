print('*** Juego de Adivinanzas ***')
import random
num = random.randint(1,50)
intentos = 10
while intentos > 0:
    print('''Podrás adivinar el número?
    ''')
    adivina = int(input('Escoge un número: '))
    if adivina > num:
        print('El número es menor\n')
        intentos -= 1
        print(f'Te quedan {intentos} intentos')
    elif adivina < num:
        print('El número es mayor\n')
        intentos -= 1
        print(f'Te quedan {intentos} intentos')
    elif adivina == num:
        print('\n----¡¡¡¡¡¡¡¡FELICIDADES GANASTE EL JUEGO!!!!!!!!----\n')
    else:
        print('Error')
else:
    print('LO SIENTO, PERDISTE :(')