from exercicios113_a_115C import sistema_de_cadastro_ex115

nome_do_arquivo = input('Digite o nome do arquivo: ')

txt = input('Digite o texto a ser adcionado: ')
try:
    open(f'exercicios113_a_115C/sistema_de_cadastro_ex115/arquivos_de_texto/{nome_do_arquivo}')
except FileNotFoundError:
    print(f'\033[31mArquivo: {nome_do_arquivo} está sendo criado agora!\033[m')
else:
    print('f\033[32mArquivo já está criado:\033[m')

sistema_de_cadastro_ex115.CriacaoDoArquivo(nome_do_arquivo, txt)

