a = []
while True:
    z = int(input('digite um numero:'))
    a.append(z)
    print(f'valor {z} adicionado com sucesso!')

    while True:
        k = str(input('deseja continuar? [S/N]')).strip().upper()
        if k == 'S' or k == 'N' or k == 's' or k == 'n':
            break

    if k == 'N':
        break
a.sort(reverse=True)
print(f'a quantidade de elementos na lista é: {len(a)}')
print(f'a lista reversa é : {a}')
if 5 in a:
    print(f'existe sim o numero {5} na lista "a"')
else:
    print(f'não existe o numero {5} na lista "a"')
