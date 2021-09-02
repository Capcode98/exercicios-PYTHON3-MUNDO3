a = []
while True:
    k = 0
    resposta = str(input('digite uma expressao qualquer:')).strip()

    for itens in resposta:

        if itens == '(':
            a.append(resposta)

        elif itens == ')':

            if len(a) == 0:
                print('expressao invalida')
                k = 1
                break

            elif len(a) != 0:
                a.pop()

    if len(a) > 0:
        print('''Expressao invalida
        Tente novamente!!''')

    elif len(a) == 0 and resposta[0] != ')' and resposta.count('(') == resposta.count(')') and k == 0:
        print('Expressao valida!!')
        print(a)

    while True:
        c = str(input('deseja continuar ? [S/N] ')).strip().upper()

        if c == 'S' or c == 'N':
            break

    if c == 'N':
        break
