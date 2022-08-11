def aumentar(valor, aumento):
    valor += valor * aumento / 100
    return valor


def diminuir(valor, diminuicao):
    valor -= valor * diminuicao / 100
    return valor


def metade(valor):
    valor = valor / 2
    return valor


def dobro(valor):
    valor = valor * 2
    return valor


def moeda(valor):
    return f'R$ {valor}'
