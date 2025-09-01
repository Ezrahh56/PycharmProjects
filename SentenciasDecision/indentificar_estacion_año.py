print('*** Indetificar la estación del año')

mes = int(input('Número del mes: '))

if 3 <= mes <= 5:
    print('Es Primavera')
elif 6 <= mes <= 8:
    print('Es Verano')
elif 9 <= mes <= 11:
    print('Es Otoño')
elif mes == 1 or mes == 2 or mes == 12:
    print('Es Invierno')
else:
    print('Estación desconocida')