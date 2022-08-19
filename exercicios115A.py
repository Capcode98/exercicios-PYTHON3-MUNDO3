from exercicios113_a_115C import arquivos_txt_ex115A

nome_do_arquivo = input('Digite o nome do arquivo: ')

txt = input('Digite o texto a ser adcionado: ')
try:
    open(f'exercicios113_a_115C/arquivos_txt_ex115A/arquivos_de_texto/{nome_do_arquivo}')
except FileNotFoundError:
    print(f'\033[31mArquivo: {nome_do_arquivo} está sendo criado agora!\033[m')
else:
    print('f\033[32mArquivo já está criado:\033[m')

arquivos_txt_ex115A.CriacaoDoArquivo(nome_do_arquivo, txt)

