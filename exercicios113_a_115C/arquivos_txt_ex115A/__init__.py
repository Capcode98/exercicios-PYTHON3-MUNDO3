from os import remove


def AdicionarPessoas(nome_do_arquivo, txt=''):

    nome_do_arquivo = f'exercicios113_a_115C/arquivos_txt_ex115A/arquivos_de_texto/{nome_do_arquivo}'

    intencao = "a"

    try:
        open(nome_do_arquivo, intencao)

    except Exception as error:

        return print(f"\033[31mERRO {error.__class__}: Arquivo não encontrado,"
                     f" verifique e tente novamente, por favor! \033[m")

    else:

        with open(nome_do_arquivo, intencao) as arquivo:

            texto = arquivo.seek(0, 0)

            if texto != "":

                arquivo.write(txt + '\n')

            else:

                arquivo.write(txt)

        for linha in arquivo.readlines():

            print(f'~~> {linha}', end='')
        print()
        return print(f'\033[32mArquivo encontrado e texto adicionado com sucesso!\033[m\nnome do arquivo: '
                     f'{nome_do_arquivo}')

    finally:
        arquivo.close()


def LeituraDePessoas(nome_do_arquivo):

    nome_do_arquivo = f'exercicios113_a_115C/arquivos_txt_ex115A/arquivos_de_texto/{nome_do_arquivo}'

    intencao = "r"

    try:
        open(nome_do_arquivo, intencao)

    except Exception as error:

        return print(f"\033[31mERRO {error.__class__}: Arquivo não encontrado,"
                     f" verifique e tente novamente, por favor! \033[m")

    else:

        with open(nome_do_arquivo, intencao) as arquivo:

            for linha in arquivo.readlines():

                print(f'~~> {linha}', end='')

            print()

            return print(f'\033[32mArquivo encontrado e texto lido com sucesso!\033[m\nnome do arquivo: '
                         f'{nome_do_arquivo}')

    finally:

        arquivo.close()


def CriacaoDoArquivo(nome_do_arquivo, txt=''):

    nome_do_arquivo = f'exercicios113_a_115C/arquivos_txt_ex115A/arquivos_de_texto/{nome_do_arquivo}'

    intencao = "w"

    try:

        open(nome_do_arquivo, intencao)

    except Exception as error:

        return print(f"\033[31mERRO {error.__class__}: Arquivo não encontrado,"
                     f" verifique e tente novamente, por favor! \033[m")

    else:

        with open(nome_do_arquivo, intencao) as arquivo:

            arquivo.write(txt.upper() + '\n')

            return print(f'\033[32mArquivo criado e Titulo adicionado com sucesso!\033[m\nnome do arquivo: '
                         f'{nome_do_arquivo}')

    finally:

        arquivo.close()


def DeletarArquivo(nome_do_arquivo):
    nome_do_arquivo = f'exercicios113_a_115C/arquivos_txt_ex115A/arquivos_de_texto/{nome_do_arquivo}'
    try:
        remove(nome_do_arquivo)
    except Exception as error:
        return print(f"\033[31mERRO {error.__class__}: Arquivo não encontrado,"
                     f" verifique e tente novamente, por favor! \033[m")
    else:
        return print(f'\033[32mArquivo removido com sucesso!\033[m\nnome do arquivo: '
                     f'{nome_do_arquivo}')
