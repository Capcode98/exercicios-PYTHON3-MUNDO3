def ficha(nome='<desconhecido>',  gols=0):
    """
    :param nome: Nome do jogador a ser adicionado no dicionário
    :param gols: quantidade de gols marcados pelo jogador
    :return: retorna o print com as informações obtidas do dicionário
    """

    informacoes = dict()

    informacoes['Nome: '] = nome
    informacoes['Gols: '] = gols

    return print(f'O jogador: {informacoes["Nome: "]} fez {informacoes["Gols: "]} Gols.')


while True:

    nome_1 = input('Digite o nome do jogador: ').lstrip().rstrip().upper()

    if nome_1.isalpha() is True or nome_1 == "":

        break

while True:

    gols_1 = input(f'digite a quantidade de gols que fez o jogador {nome_1}: ').strip()

    if gols_1.isnumeric() is True or gols_1 == "":

        break

if nome_1 == "" and gols_1 == "":
    ficha()
elif nome_1.isalpha() is True and gols_1 == "":
    ficha(nome_1)
elif gols_1.isnumeric() is True and nome_1 == "":
    ficha(gols=int(gols_1))
elif nome_1.isalpha() is True and gols_1.isnumeric() is True:
    ficha(nome_1, int(gols_1))
