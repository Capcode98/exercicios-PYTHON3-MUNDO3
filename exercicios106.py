from time import sleep


def PyHelp(fun):

    txt = 'SISTEMA DE AJUDA PyHelp:'
    print(f'^' * (len(txt) + 2))
    print(f"SISTEMA DE AJUDA PyHelp:")
    print(f'^' * (len(txt) + 2))
    sleep(0.5)
    print('\033[1;33m')
    help(fun)
    print('\033[m')


PyHelp(input(":"))
