a = []
while True:
    z = int(input('digite um numero:'))
    if z in a:
        print('esse valor ja foi digitado tente outro:')
    else:
        a.append(z)
        print(f'valor {z} adicionado com sucesso!')

    while True:
        k = str(input('deseja continuar? [S/N]')).strip().upper()
        if k == 'S' or k == 'N' or k == 's' or k == 'n':
            break

    if k == 'N':
        break

a.sort()
print(a)
