pessoas = list()
pessoas_idosas = list()
pessoa = list()

mulheres = dict()
nomes = dict()
sexos = dict()
idades = dict()

z = 0

while True:

    nomes[f'nome {z}'] = str(input('digite o nome:')).strip()
    sexos[f'sexo {z}'] = str(input('digite o sexo:')).strip().upper()
    idades[z] = int(str(input('digite a idade:')).strip())

    pessoa.append(nomes[f'nome {z}'])
    pessoa.append(sexos[f'sexo {z}'])
    pessoa.append(idades[z])

    if sexos[f'sexo {z}'] == 'F':

        mulheres[f'{z}'] = nomes[f'nome {z}']
        print(z)
        print(mulheres)

    pessoas.append(pessoa[:])

    pessoa.clear()

    z += 1

    while True:
        r = str(input('deseja continuar? [S/N]')).strip().upper()

        if r == 'S' or r == 'N':
            break
    if r == 'N':
        break


media = 0

for c in idades.values():
    media += c

Media = media/z

for k, v in idades.items():
    if v > Media:

        pessoas_idosas.append(nomes[f'nome {k}'])
        pessoas_idosas.append(sexos[f'sexo {k}'])
        pessoas_idosas.append(idades[k])

print(f'A quantidade de pessoas cadastradas foram {z}.\nA média de idade do grupo foi {Media} anos.\n'
      f'As mulheres cadastradas foram: {mulheres.values()}.\n'
      f'As pessoas com idade acima da media foram: {pessoas_idosas}.')
