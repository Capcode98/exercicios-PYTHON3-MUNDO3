from exercicios113_a_115C.sistema_de_cadastro_ex115 import funcoes_menu_sistema_cad_ex155
from time import sleep

while True:
    funcoes_menu_sistema_cad_ex155.Menu()
    try:
        opcao = int(input('Digite o numero correspondente a sua opção: '))
    except ValueError:
        print("Digite apenas numeros do tipo inteiro")
    except KeyboardInterrupt:
        print('O usuario não digitou nenhum valor, por conta disso o sistema será incerrado em 5 segundos, '
              'para cancelar digite o valor 0 ao final da contagem: ')
        funcoes_menu_sistema_cad_ex155.ContagemRegressiva()

        print('Voltando para o Programa normal!')

    else:
        if opcao == 1:
            pass
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == -1:
            pass
        else:
            pass
