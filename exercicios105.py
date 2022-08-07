def notas(* num, sit=False):

    dicionario = dict()

    k = 0
    media = 0

    for c in num:
        dicionario[f'nota {k}'] = float(c)
        media += c
        k += 1

    dicionario['media'] = media/k

    if sit:

        if 4 <= dicionario['media'] >= 0:
            dicionario['situação'] = 'Ruim'

        elif 7 < dicionario['media'] > 4:
            dicionario['situação'] = 'Razoavel'

        elif 10 <= dicionario['media'] >= 7:
            dicionario['situação'] = 'Boa'

        return print(dicionario)

    else:
        return print(dicionario)


notas(6.4, 7.9, 8, 3, sit=True)
