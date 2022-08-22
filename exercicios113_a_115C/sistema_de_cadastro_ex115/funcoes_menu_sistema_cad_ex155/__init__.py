from time import sleep


def Menu():
    print('-' * 45)
    print(f'{"MENU PRINCIPAL":^45}')
    print('-' * 45)
    print(f'\033[35m 1 :\033[m\033[32m ~Ver pessoas cadastradas!\033[m')
    print(f'\033[35m 2 :\033[m\033[33m ~Cadastrar uma nova pessoa!\033[m')
    print(f'\033[35m 3 :\033[m\033[34m ~Sair do Sistema!\033[m')


def ContagemRegressiva():
    print('Contagem Regressiva Iniciada! ')
    for i in range(5, -1, -1):
        sleep(1)
        print(f'Contagem Regressiva: {i}')
    return 0


def PegarAOpcao():
    p = int(input('Digite o numero correspondente a sua opção: '))
    return p
