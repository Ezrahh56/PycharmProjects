print('*** Cálculo de Área y Perímetro de un rectángulo ***')

base = int(input('Cuál es la medida de la base rectángulo: '))
altura = int(input('Cuál es la medida de la altura del rectángulo: '))

area = base * altura
perimetro = (base*2)+(altura*2)

print(f'El perímetro del rectángulo es: {perimetro}\nEl área del rectángulo es: {area}')
