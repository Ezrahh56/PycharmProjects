print('*** Aplicación en Python ***')

numero = False
while not numero:
    print('''Operaciones que puedes realizar:
    1. Suma 
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')
    opcion = int(input('Escoge una opción: '))
    if opcion == 1:
        a = float(input('Dame el valor 1: '))
        b = float(input('Dame el valor 2: '))
        r = a + b
        print(f'El resultado de la suma es: {r:.2f}')
    elif opcion == 2:
        a = float(input('Dame el valor 1: '))
        b = float(input('Dame el valor 2: '))
        r = a - b
        print(f'El resultado de la resta es: {r:.2f}')
    elif opcion == 3:
        a = float(input('Dame el valor 1: '))
        b = float(input('Dame el valor 2: '))
        r = a * b
        print(f'El resultado de la multiplicación es: {r:.2f}')
    elif opcion == 4:
        a = float(input('Dame el valor 1: '))
        b = float(input('Dame el valor 2: '))
        r = a / b
        print(f'El resultado de la división es: {r:.2f}')
    elif opcion == 5:
        print(f'Saliendo de la calculadora Python')
    else:
        print('Escoja una opción válida...')
else:
    print('Error en el sistema')