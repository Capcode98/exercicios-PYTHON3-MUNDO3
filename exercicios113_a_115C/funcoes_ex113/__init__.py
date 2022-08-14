def leiaint(txt):
    numero = txt

    while True:
        try:
            int(numero)

        except (TypeError, ValueError):
            print(f"\033[31mERRO: Tipo de dado incorreto, digite apenas Números, por favor! \033[m")
            numero = input('Digite um valor Inteiro: ')

        else:
            print('\033[32mNúmero aceito com sucesso!\033[m')
            return int(numero)

        finally:
            pass


def leiafloat(txt):
    numero = txt

    while True:
        try:
            float(numero)

        except (TypeError, ValueError):
            print(f"\033[31mERRO: Tipo de dado incorreto, digite apenas Números, por favor! \033[m")
            numero = input('Digite um valor racional: ')

        else:
            print('\033[32mNúmero aceito com sucesso!\033[m')
            return float(numero)

        finally:
            pass
