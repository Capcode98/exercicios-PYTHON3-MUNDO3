aluno = dict()
while True:
    aluno['Nome'] = str(input('qual o nome do aluno?')).strip().title()
    aluno['Média'] = float(str(input('qual a media do aluno?')).strip())
    if aluno['Média'] >= 7:
        print(f'O nome é {aluno["Nome"]} \n A media é {aluno["Média"]} \n E o aluno foi aprovado!')
        print(aluno)
    else:
        print(f'O nome é {aluno["Nome"]} \n A media é {aluno["Média"]} \n E o aluno foi reprovado!')
        print(aluno)

    while True:
        r = str(input('deseja continuar? [S/N]')).strip().upper()

        if r == 'S' or r == 'N':
            break

    if r == 'N':
        break
    else:
        del aluno['Nome']
        del aluno['Média']
