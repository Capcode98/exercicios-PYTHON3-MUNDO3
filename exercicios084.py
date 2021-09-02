pessoas = list()
dados = list()

while True:

    dados.append(str(input('digite um nome:')).strip().capitalize())
    dados.append(float(str(input('digite seu peso:')).strip()))
    pessoas.append(dados[:])
    dados.clear()

    while True:
        d = str(input('deseja continuar? [S/N]')).strip().upper()
        if d in 'S' or d in 'N':
            break
    if d == 'N':
        break

p = 0
M = list()
m = list()

for k in range(0, len(pessoas)):

    if k == 0:
        M.append(pessoas[k][0])
        M.append(pessoas[k][1])
        m.append(pessoas[k][0])
        m.append(pessoas[k][1])

    else:
        if pessoas[k][1] > M[1]:
            M.pop()
            M.pop()
            M.append(pessoas[k][0])
            M.append(pessoas[k][1])

        elif pessoas[k][1] == M[1]:
            M.append(pessoas[k][0])
            M.append(pessoas[k][1])

        elif pessoas[k][1] < m[1]:
            m.pop()
            m.pop()
            m.append(pessoas[k][0])
            m.append(pessoas[k][1])

        elif pessoas[k][1] == m[1]:
            m.append(pessoas[k][0])
            m.append(pessoas[k][1])

print(f'''a quantidade de pessoas cadastradas foram: {len(pessoas)} pessoas.
 as pessoas com maiores pesos sao: {M}.
 as pessoas com menores pesos sao: {m}.''')
