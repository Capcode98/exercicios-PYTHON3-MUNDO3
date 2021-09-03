from datetime import date
atual = date.today().year

funcionario = dict()

funcionario['NOME'] = str(input('Nome:')).strip().capitalize()
funcionario['DATA'] = int(str(input('Ano de Nascimento:')).strip().capitalize())
funcionario['CTPS'] = int(str(input('CTPS:')).strip().capitalize())
funcionario['IDADE'] = atual - funcionario['DATA']

if funcionario['CTPS'] == 0:

    print(f'o nome do funcionario: {funcionario["NOME"]}\na idade do funcionario: {funcionario["IDADE"]}\n'
          f'o funcionario não tem um CTPS')

else:

    funcionario['ano de contratação'] = int(str(input('Ano de contratação:')).strip().capitalize())
    funcionario['Salario'] = float(str(input('Salario:')).strip().capitalize())
    funcionario['tempo de contribuição'] = atual - funcionario['ano de contratação']
    funcionario['tempo que falta'] = 35 - funcionario['tempo de contribuição']

    print(f'o nome do funcionario: {funcionario["NOME"]}\na idade do funcionario: {funcionario["IDADE"]}\n'
          f'o CTPS do funcionario: {funcionario["CTPS"]}\no salario do funcionario: {funcionario["Salario"]}\n'
          f'o funcionario ja trabalhou: {funcionario["tempo de contribuição"]}\nfalta {funcionario["tempo que falta"]}'
          f' anos para o funcionario se aposentar!')
