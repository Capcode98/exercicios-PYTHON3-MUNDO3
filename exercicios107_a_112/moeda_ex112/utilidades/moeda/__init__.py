def aumentar(valor, aumento, formatacao=True):
    valor += valor * aumento / 100
    if formatacao is True:
        return print(f'{aumento}% de aumento: {moeda(valor)}')
    else:
        return valor


def diminuir(valor, diminuicao, formatacao=True):
    valor -= valor * diminuicao / 100
    if formatacao is True:
        return print(f'{diminuicao}% de redução: {moeda(valor)}')
    else:
        return valor


def metade(valor, formatacao=True):
    valor = valor / 2
    if formatacao is True:
        return print(f'Metade do preço: {moeda(valor)}')
    else:
        return valor


def dobro(valor, formatacao=True):
    valor = valor * 2
    if formatacao is True:

        return print(f'Dobro do preço: {moeda(valor)}')

    else:
        return valor


def moeda(valor):
    return f'R$ {valor}'


def resumo(a, b, c):

    print("-" * len(f"Preço analisado: {dobro(a, False)}"))
    print(f'{"RESUMO DO VALOR":^{len(f"Preço analisado: {dobro(a, False)}")}}')
    print("-" * len(f"Preço analisado: {dobro(a, False)}"))
    print(f'Preço analisado: {moeda(a)}')
    dobro(a)
    metade(a)
    aumentar(a, b)
    diminuir(a, c)

    print("-" * len(f'Preço analisado: {dobro(a,False)}'))
