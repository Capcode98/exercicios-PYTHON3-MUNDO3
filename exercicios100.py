from random import randint


def sorteia():
    a = list()
    for c in range(0, 5):
        a.append(randint(0, 100))
    print(a)
    return a


def somapar(a):
    soma = 0
    for c in a:
        if c % 2 == 0:
            soma += c
    return print(soma)


somapar(sorteia())
