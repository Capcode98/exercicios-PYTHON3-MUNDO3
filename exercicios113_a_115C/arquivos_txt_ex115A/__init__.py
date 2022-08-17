def arquivos(nome_do_arquivo, txt='', opcao=0):

    nome_do_arquivo = f'exercicios113_a_115C/arquivos_txt_ex115A/arquivos_de_texto/{nome_do_arquivo}'

    if opcao == 0:
        a = 'r'
        with open(nome_do_arquivo, a) as arquivo:

            texto_em_linhas = arquivo.readline()
            for linha in texto_em_linhas:
                print(linha)

    elif opcao == 1:
        a = 'w'
        with open(nome_do_arquivo, a) as arquivo:

            arquivo.write(txt)

    elif opcao == 2:
        a = 'a'
        with open(nome_do_arquivo, a) as arquivo:

            arquivo.write('\n' + txt)

    else:
        pass
