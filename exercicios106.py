from time import sleep


cores = {'normal': '\033[m',
         'vermelho': '\033[m',
         'verde': '\033[m',
         'amarelo': '\033[m',
         'azul': '\033[m',
         'roxo': '\033[m',
         'branco': '\033[m'}


def PyHelp(fun):

    print('\033[1;33m')
    help(fun)
    print('\033[m')


def titulo(txt='SISTEMA DE AJUDA PyHelp:', cor=0):

    print(f'{cor}^' * (len(txt) + 4))
    print(f"  {txt}")
    print(f'{cor}^' * (len(txt) + 4))
    sleep(0.5)


PyHelp(input(":"))
