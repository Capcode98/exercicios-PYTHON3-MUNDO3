from time import sleep


def Menu():
    print('-' * 45)
    print(f'{"MENU PRINCIPAL":^45}')
    print('-' * 45)


def ContagemRegressiva(s):
    s = 0
    while s != 5:
        sleep(1)
        print(f'Contagem Regressiva Iniciada!\n {s} segundos!')