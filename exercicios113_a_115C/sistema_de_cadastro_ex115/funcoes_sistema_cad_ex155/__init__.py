from os import remove


def AdicionarPessoas(nome_do_arquivo, txt=''):

    nome_do_arquivo = f'exercicios113_a_115C/sistema_de_cadastro_ex115/arquivos_de_texto/{nome_do_arquivo}'

    intencao = "+a"

    try:
        open(nome_do_arquivo, intencao, encoding='utf-8')

    except Exception as error:

        return print(f"\033[31mERRO {error.__class__}: Arquivo não encontrado,"
                     f" verifique e tente novamente, por favor! \033[m")

    else:

        with open(nome_do_arquivo, intencao, encoding='utf-8') as arquivo:

            texto = arquivo.seek(0, 0)

            if texto != "":

                arquivo.write(txt + '\n')

            else:

                arquivo.write(txt)

    finally:
        arquivo.close()


def LeituraDePessoas(nome_do_arquivo):

    nome_do_arquivo = f'exercicios113_a_115C/sistema_de_cadastro_ex115/arquivos_de_texto/{nome_do_arquivo}'

    intencao = "r"

    try:
        open(nome_do_arquivo, intencao, encoding='utf-8')

    except Exception as error:

        return print(f"\033[31mERRO {error.__class__}: Arquivo não encontrado,"
                     f"\nverifique se arquivo de fato existe e tente novamente,"
                     f"\npor favor! \033[m")

    else:

        with open(nome_do_arquivo, intencao, encoding='utf-8') as arquivo:

            print('-' * 45)

            for linha in arquivo.readlines():

                print(f'~~> {linha}', end='')

            print('-' * 45)

            return print(f'\033[32mArquivo encontrado e texto lido com sucesso!\033[m')


def CriacaoDoArquivo(nome_do_arquivo, txt=''):

    nome_do_arquivo = f'exercicios113_a_115C/sistema_de_cadastro_ex115/arquivos_de_texto/{nome_do_arquivo}'

    intencao = "w"

    try:

        open(nome_do_arquivo, intencao, encoding='utf-8')

    except Exception as error:

        return print(f"\033[31mERRO {error.__class__}: Arquivo não encontrado,"
                     f" verifique e tente novamente, por favor! \033[m")

    else:

        with open(nome_do_arquivo, intencao, encoding='utf-8') as arquivo:

            arquivo.write(f'{txt.upper():^45}' + '\n')

            return print(f'\033[32mArquivo criado e Titulo adicionado com sucesso!\033[m')

    finally:

        arquivo.close()


def DeletarArquivo(nome_do_arquivo):

    nome_do_arquivo = f'exercicios113_a_115C/sistema_de_cadastro_ex115/arquivos_de_texto/{nome_do_arquivo}'

    try:

        remove(nome_do_arquivo)

    except FileNotFoundError:

        return print(f"\033[31mERRO 404: Arquivo não encontrado,"
                     f" verifique e tente novamente, por favor! \033[m")

    else:

        return print(f'\033[32mArquivo removido com sucesso!\033[m')
