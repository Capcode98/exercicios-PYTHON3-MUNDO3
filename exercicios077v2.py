a = ('Joao', 'Maria', 'Carlos', 'Jucelino', 'Romeu', 'Clara', 'Joaquina')

for i in a:
    print(f'\n No nome {i} tem as seguintes vogais e na segunte ordem: ', end='')
    for k in i:
        if k in 'aAeEiIoOuU':
            print(f'{k}', end=' ')
