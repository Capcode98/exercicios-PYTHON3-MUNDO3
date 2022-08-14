from exercicios113_a_115C import funcoes_ex113

try:
    funcoes_ex113.leiaint(input('Digite um valor Inteiro: '))

except KeyboardInterrupt:
    print(f"\033[31mERRO: O usuario prefiriu não digitar um valor! \033[m")
    print("Volte Sempre!")

try:
    funcoes_ex113.leiafloat(input('Digite um valor Racional: '))

except KeyboardInterrupt:
    print(f"\033[31mERRO: O usuario prefiriu não digitar um valor! \033[m")
    print("Volte Sempre!")
