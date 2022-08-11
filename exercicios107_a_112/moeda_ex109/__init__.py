def aumentar(valor, aumento, formatacao=True):
    valor += valor * aumento / 100
    if formatacao is True:
        return moeda(valor)
    else:
        return valor


def diminuir(valor, diminuicao, formatacao=True):
    valor -= valor * diminuicao / 100
    if formatacao is True:
        return moeda(valor)
    else:
        return valor


def metade(valor, formatacao=True):
    valor = valor / 2
    if formatacao is True:
        return moeda(valor)
    else:
        return valor


def dobro(valor, formatacao=True):
    valor = valor * 2
    if formatacao is True:
        return moeda(valor)
    else:
        return valor


def moeda(valor):
    return f'R$ {valor}'
