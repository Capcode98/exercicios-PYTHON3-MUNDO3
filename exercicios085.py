numeros = list()
numeros_pares = list()
numeros_impares = list()
numero = list()

while True:
    numero.append(int(input('digite um numero:')))

    if numero[0] % 2 == 0:
        numeros_pares.append(numero[0])

    else:
        numeros_impares.append(numero[0])

    del numero
    numero = list()

    while True:
        d = str(input('deseja continuar? [S/N]')).strip().upper()

        if d in 'S' or d in 'N':
            break

    if d == 'N':
        break

numeros.append(numeros_impares[:])
numeros.append(numeros_pares[:])
numeros_pares.sort()
numeros_impares.sort()

print(f'os numeros digitados foram: {numeros} \n'
      f'os numeros pares digitados foram: {numeros_pares}\n'
      f'os numeros impares digitados foram: {numeros_impares}')
