from exercicios113_a_115C.sistema_de_cadastro_ex115.funcoes_sistema_cad_ex155 import CriacaoDoArquivo, \
    AdicionarPessoas, DeletarArquivo, LeituraDePessoas

nome_do_arquivo = input('Digite o nome do arquivo: ')

txt = input('Digite o texto a ser adcionado: ')

try:

    open(f'exercicios113_a_115C/sistema_de_cadastro_ex115/funcoes_sistema_cad_ex155/arquivos_de_texto/'
         f'{nome_do_arquivo}')

except FileNotFoundError:

    print(f'\033[31mArquivo: {nome_do_arquivo} está sendo criado agora!\033[m')

else:

    print('f\033[32mArquivo já está criado:\033[m')

CriacaoDoArquivo(nome_do_arquivo, txt)

