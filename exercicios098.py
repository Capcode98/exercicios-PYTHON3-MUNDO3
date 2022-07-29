from time import sleep


def contador(inicio, fim, passo):
    if inicio < fim and passo > 0:
        for c in range(inicio, fim + 1, passo):
            print(c, end=" ")
            sleep(0.5)
        print(" Fim!")

    elif inicio > fim and passo < 0:
        for c in range(inicio, fim - 1, passo):
            print(c, end=" ")
            sleep(0.5)
        print(" Fim!")

    elif passo == 0 or type(passo) == 'NoneType':
        passo = 1
        print(f'passo inválido será considerado "PASSO = {passo}"')
        for c in range(inicio, fim + 1, passo):
            print(c, end=" ")
            sleep(0.5)
        print(" Fim!")

    elif passo < 0 and inicio <= fim:  # INICIO = 5; FINAL = 10; PASSO = -1
        passo = passo * (-1)
        print(f'passo inválido será considerado "PASSO = {passo}"')
        for c in range(inicio, fim + 1, passo):
            print(c, end=" ")
            sleep(0.5)
        print(" Fim!")

    elif passo > 0 and inicio >= fim:  # INICIO = 10; FINAL = 5; PASSO = 1
        passo = passo * (-1)
        print(f'passo inválido será considerado "PASSO = {passo}"')
        for c in range(inicio, fim - 1, passo):
            print(c, end=" ")
            sleep(0.5)
        print(" Fim!")


while True:

    while True:
        Inicio = input('Inicio: ')
        Fim = input('Fim: ')
        Passo = input('Passo: ')

        if Inicio.isnumeric() == Fim.isnumeric() == Passo.isnumeric() is True:
            break

        else:
            print('valor incorreto, DIGITE APENAS VALORES NUMERICOS!!')

    contador(int(Inicio), int(Fim), int(Passo))

    while True:
        stop = input("deseja continuar (S/N): ").strip().upper()
        if stop == "S" or stop == "N":
            break
    if stop == "N":
        break
