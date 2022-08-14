def leiaint(txt):
    numero = txt

    while True:
        try:
            int(numero)

        except KeyboardInterrupt:
            print(f"\033[31mERRO: O usuario prefiriu não digitar um valor! \033[m")
            numero = input('Digite um valor Inteiro: ')

        except (TypeError, ValueError):
            print(f"\033[31mERRO: Tipo de dado incorreto, digite apenas Números, por favor! \033[m")
            numero = input('Digite um valor Inteiro: ')

        else:
            print('\033[32mNúmero aceito com sucesso!\033[m')
            print('volte logo')
            return int(numero)


def leiafloat(txt):
    numero = txt

    while True:
        try:
            float(numero)

        except KeyboardInterrupt:
            print(f"\033[31mERRO: O usuario prefiriu não digitar um valor! \033[m")
            numero = input('Digite um valor racional: ')

        except (TypeError, ValueError):
            print(f"\033[31mERRO: Tipo de dado incorreto, digite apenas Números, por favor! \033[m")
            numero = input('Digite um valor racional: ')

        else:
            print('\033[32mNúmero aceito com sucesso!\033[m')
            print('volte logo')
            return float(numero)
