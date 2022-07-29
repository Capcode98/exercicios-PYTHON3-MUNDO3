from random import randint
from time import sleep


def sorteia():
    a = list()
    print('Sorteando 5 valores da Lista: ', end=" ")
    for c in range(0, 5):
        sleep(0.5)
        x = randint(0, 100)
        print(f'{x}', end=" ")
        a.append(x)
    sleep(0.5)
    print("Pronto! \n")
    return a


def somapar(a):
    soma = 0
    for c in a:
        if c % 2 == 0:
            soma += c
    return print(f'a soma par foi: {soma}')


somapar(sorteia())
