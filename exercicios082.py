
a = list()
p = list()
i = list()
while True:
    r = int(str(input('digite um numero:')).strip())
    a.append(r)
    while True:
        c = str(input('deseja continuar [S/N]')).strip().upper()
        if c in 'S' or c in 'N':
            break
    if c == 'N':
        break
for z in a:
    if z % 2 == 0:
        p.append(z)
    else:
        i.append(z)

print(f'os numeros digitados foram: {a}, os numeros pares digitados foram: {p} ,  os numeros impares digitados foram: '
      f'{i}')
