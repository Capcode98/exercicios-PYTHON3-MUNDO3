pessoas = list()
mulheres = list()
pessoas_idosas = list()

nomes = dict()
sexos = dict()
idades = dict()

k = 0

while True:
    pessoa = list()

    nomes[f'nome {k}'] = str(input('digite o nome:')).strip()
    sexos[f'sexo {k}'] = str(input('digite o sexo:')).strip()
    idades[f'idade {k}'] = int(str(input('digite a idade:')).strip())

    pessoa.append(nomes[f'nome {k}'])
    pessoa.append(sexos[f'sexo {k}'])
    pessoa.append(idades[f'idade {k}'])

    pessoas.append(pessoa[:])

    pessoa.clear()

    k += 1

    while True:
        r = str(input('deseja continuar? [S/N]')).strip().upper()

        if r == 'S' or r == 'N':
            break
    if r == 'N':
        break


media = 0

for c in idades.values():
    media += c

Media = media/k

print(f'A quantidade de pessoas cadastradas foram {k}\nA média de idade do grupo foi {Media}\n'
      f'As mulheres cadastradas foram: {mulheres}\nAs pessoas com idade a cima da media foram: {pessoas_idosas}')
print(f'{pessoas} \n {nomes}\n{sexos}\n{idades}')
