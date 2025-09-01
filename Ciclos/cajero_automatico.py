print('*** Aplicación de Cajero Automático ***')

saldo = 1000.00
while saldo >= 0:
    print(f'''Operaciones que puedes realizar:
    1. Consultar Saldo
    2. Retirar
    3. Depositar
    4. Salir''')
    opcion = int(input('Escoge una opción: '))
    if opcion == 1:
        print(f'Tu sueldo actual es de ${saldo:.2f\n}')
    elif opcion == 2:
        retiro = float(input('Ingresa el monto a retirar:'))
        if saldo < retiro:
            print(f'No cuentas con saldo suficiente. Saldo actual ${saldo:.2f\n}')
        else:
            saldo -= retiro
            print(f'Tu nuevo saldo es: ${saldo:.2f\n}')
    elif opcion == 3:
        deposito = float(input('Ingresa el monto a depositar: '))
        saldo += deposito
        print(f'Tu nuevo saldo es: {saldo:.2f\n}')
    elif opcion == 4:
        print('Saliendo del cajero automático...\n')
    else:
        print('Ingrese una opción válido: \n')
else:
    print('Error en el sistema...\n')