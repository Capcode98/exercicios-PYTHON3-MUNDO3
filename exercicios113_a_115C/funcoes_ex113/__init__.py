def leiaint(txt):
    numero = txt

    while True:
        try:
            int(numero)

        except KeyboardInterrupt:
            print(f"\033[31mERRO: O usuario prefiriu não digitar um valor! \033[m")

        except:
            print(f"\033[31mERRO: Tipo de dado incorreto, digite apenas Números, por favor! \033[m")

        else:
            print('volte logo')
            return numero
            break




