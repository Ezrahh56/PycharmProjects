print('*** Sistema de Calificaciones ***')

valor = float(input('Colocar nota a convertir: '))

if 9 <= valor <= 10:
    print('Su nota es A')
elif 8 <= valor < 9:
    print('Su nota es B')
elif 7 <= valor < 8:
    print('Su nota es C')
elif 6 <= valor < 7:
    print('Su nota es D')
elif 0 <= valor < 6:
    print('Su nota es D')
else:
    print('Valor desconocido')