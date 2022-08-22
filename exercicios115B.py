from exercicios113_a_115C.sistema_de_cadastro_ex115 import funcoes_menu_sistema_cad_ex155
from exercicios113_a_115C.sistema_de_cadastro_ex115.funcoes_sistema_cad_ex155 import CriacaoDoArquivo, \
    AdicionarPessoas, DeletarArquivo, LeituraDePessoas


while True:

    funcoes_menu_sistema_cad_ex155.Menu()

    try:

        opcao = funcoes_menu_sistema_cad_ex155.PegarAOpcao()

    except ValueError:

        print("Digite apenas numeros do tipo inteiro")

    except KeyboardInterrupt:

        print('\nO usuario não digitou nenhum valor, por conta disso o sistema será incerrado em 5 segundos: ')

        estado = funcoes_menu_sistema_cad_ex155.ContagemRegressiva()

        if estado == 0:

            print('Programa Finalizado!')

            break

    else:

        nome_do_arquivo = input('Digite o nome do arquivo: ')

        txt = input('Digite o texto a ser adcionado: ')

        try:

            open(f'exercicios113_a_115C/sistema_de_cadastro_ex115/funcoes_sistema_cad_ex155/arquivos_de_texto/'
                 f'{nome_do_arquivo}')

        except FileNotFoundError:

            print(f'\033[31mArquivo: {nome_do_arquivo} está sendo criado agora!\033[m')

        else:

            print('f\033[32mArquivo já está criado:\033[m')

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
