def leiaint(txt):
    while True:
        numero = input(txt)
        if numero.isnumeric() is True:
            print('\033[32mTipo aceito com sucesso!\033[m')
            break
        else:
            print("\033[31mTipo de dado incorreto, digite apenas Números, por favor! \033[m")
    return print(numero)


leiaint('Digite um valor numérico: ')
