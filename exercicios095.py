jogador = dict()
jogadores = list()
jogador_gols = list()

while True:

    jogador['Nome'] = str(input('digite o nome do jogador: ')).strip().capitalize()
    jogador['Jogos'] = int(str(input('digite a quantidade de jogos do jogador: ')).strip().capitalize())

    tot = 0

    for c in range(0, jogador['Jogos']):

        jogador[f'partida {c + 1}'] = int(input(f'quantos gols o jogador {jogador["Nome"]} fez na {c + 1}ª partida?'))
        tot += jogador[f'partida {c + 1}']
        jogador_gols.append(jogador[f'partida {c + 1}'])

    jogador['golos'] = jogador_gols[:]
    jogador['tot'] = tot
    jogadores.append(jogador.copy())
    jogador_gols.clear()
    jogador.clear()

    while True:

        r = str(input('deseja continuar? [S/N]')).strip().upper()

        if r == 'S' or r == 'N':
            break

    if r == 'N':
        print(jogadores)
        print()
        print(jogador)

        print(f'-=' * 30)
        print(f'No.  Nome             gols         total\n')

        for k in range(0, len(jogadores)):

            print(f'{k}    {jogadores[k]["Nome"]}              {jogadores[k]["golos"]}           {jogadores[k]["tot"]}')
        print(f'-=' * 30)

        while True:

            inf = str(input('mostrar os dados de qual jogador? \n(digite "Parar" para finalizar o programa)')) \
                .capitalize().strip()

            if inf != 'Parar':

                y = int(inf)
                print(f'o jogador {jogadores[y]["Nome"]} jogou {jogadores[y]["Jogos"]} partidas.')

                for p in range(0, jogadores[y]['Jogos']):

                    print(f'    => Na partida {p + 1}, fez {jogadores[y][f"partida {p + 1}"]} gols.')

                print(f'Foi um total de {(jogadores[y]["tot"])} gols')

                print(f'A media de gols por partida de fulano foi {(jogadores[y]["tot"])/jogadores[y]["Jogos"]}')

            if inf == "Parar":

                print('<<VOLTE SEMPRE!>>\n')

                break
        break
