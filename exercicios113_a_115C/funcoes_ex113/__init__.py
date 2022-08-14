def leiaint(txt):
    numero = txt
    try:
        int(numero)

    except KeyboardInterrupt:
        print(f"\033[31mERRO: O usuario prefiriu não digitar um valor! \033[m")
        numero = input("Digite um novo valor inteiro: ")

    except Exception as erro:
        print(f"\033[31mERRO {erro.__class__}: Tipo de dado incorreto, digite apenas Números, por favor! \033[m")

    else:
        print('volte logo')
        return numero


leiaint(input("Digite um numero: "))
