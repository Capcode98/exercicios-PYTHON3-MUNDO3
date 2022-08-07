from time import sleep


cores = {'normal': '\033[m',
         'vermelho': '\033[30;41m',
         'verde': '\033[30;42m',
         'amarelo': '\033[30;43m',
         'azul': '\033[30;44m',
         'roxo': '\033[30;45m',
         'branco': '\033[7;30m'}


def PyHelp(fun):

    print(cores['amarelo'])
    help(fun)
    print(cores['normal'])


def titulo(txt='SISTEMA DE AJUDA PyHelp:', cor='vermelho'):

    print(f'{cores[str(cor)]}^' * (len(txt) + 4))
    print(f"  {txt}")
    print(f'{cores[str(cor)]}^' * (len(txt) + 4))
    sleep(0.5)


while True:

    comando = str(input(f"{cores['verde']}Digite o comando a ser procurado o manual:{cores['normal']}")).strip()

    if comando.upper() == "FIM":
        print('ATÉ LOGO!')
        break
    else:
        titulo()
        PyHelp(comando)
