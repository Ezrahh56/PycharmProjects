print('*** Break y continue')

# Ejemplo con break
print('Palabra break')
for numero in range(1, 10):
    if numero % 2 == 0: # Numero par
        print(numero)
        break # Salimos del ciclo inmediatamente
# Ejemplo con continue
print('Palabra continue')
for numero in range(1, 10):
    if numero % 2 == 1: # numero impar
        continue
    print(numero) # Numero pares