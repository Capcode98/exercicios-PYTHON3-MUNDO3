nome = list()

while True:

    pessoa = list()
    notas = list()

    pessoa.append(str(input('digite o nome do aluno: ')).lstrip().rstrip().capitalize())
    notas.append(float(str(input('digite a 1ª nota do aluno: ')).strip()))
    notas.append(float(str(input('digite a 2ª nota do aluno: ')).strip()))
    pessoa.append(notas[:])
    pessoa.append((pessoa[1][0]+pessoa[1][1])/2)

    print(f'ultima pessoa adcionada: {pessoa}')

    nome.append(pessoa[:])

    del pessoa
    del notas

    while True:
        d = str(input('deseja continuar? [S/N]')).strip().upper()

        if d in 'S' or d in 'N':
            break

    if d == 'N':
        print(f'-='*30)
        print(f'No.  Nome             MEDIA\n')
        for k in range(0, len(nome)):
            print(f'{k}    {nome[k][0]}              {nome[k][2]}')
        print(f'-='*30)
        while True:
            inf = str(input('mostrar as notas de qual aluno? \n(digite "Parar" para finalizar o programa)'))\
                .capitalize().strip()
            if inf != 'Parar':
                y = int(inf)
                print(f'notas de {nome[y][0]} sao: {nome[y][1]}')
            if inf == "Parar":
                print('<<VOLTE SEMPRE!>>\n')
                break
        break

print(nome)
