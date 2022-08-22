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

        nome_do_arquivo = 'Cad_Pessoas.txt'

        try:

            with open(f'exercicios113_a_115C/sistema_de_cadastro_ex115/arquivos_de_texto/'
                 f'{nome_do_arquivo}') as arquivo:
                pass

        except FileNotFoundError:

            CriacaoDoArquivo(nome_do_arquivo, txt='cadastro de pessoas:')

            pass

        finally:

            arquivo.close()

        if opcao == 1:

            LeituraDePessoas(nome_do_arquivo)

        elif opcao == 2:

            txt = input('Digite o NOME a ser adcionado: ')
            txt2 = input('Digite a IDADE a ser adcionado: ')

            TXT = f'{txt:<35}{txt2:>5}'

            AdicionarPessoas(nome_do_arquivo, TXT)

            LeituraDePessoas(nome_do_arquivo)

        elif opcao == 3:

            break

        elif opcao == -1:

            DeletarArquivo(nome_do_arquivo)

        else:

            pass
