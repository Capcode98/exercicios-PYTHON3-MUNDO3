def leiaint(txt):
    while True:
        numero = input(txt)
        if numero.isnumeric() is True:
            break
        else:
            print("Tipo de dado incorreto, digite apenas Números, por favor! ")
    return print(numero)


leiaint('Digite um valor numerico: ')
