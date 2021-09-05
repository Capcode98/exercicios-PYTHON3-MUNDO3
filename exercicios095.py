jogador = dict()

while True:
    
    jogador['Nome'] = str(input('digite o nome do jogador: ')).strip().capitalize()
    jogador['Jogos'] = int(str(input('digite a quantidade de jogos do jogador: ')).strip().capitalize())

    tot = 0

    for c in range(0, jogador['Jogos']):
        jogador[f'partida {c + 1}'] = int(input(f'quantos gols o jogador {jogador["Nome"]} fez na {c + 1}ª partida?'))
        tot += jogador[f'partida {c + 1}']

    while True:
        r = str(input('deseja continuar? [S/N]')).strip().upper()

        if r == 'S' or r == 'N':
            break
    if r == 'N':
        break


print(f'o jogador {jogador["Nome"]} jogou {jogador["Jogos"]} partidas.')

for k in range(0, jogador['Jogos']):

    print(f'    => Na partida {k+1}, fez {jogador[f"partida {k+1}"]} gols.')

print(f'Foi um total de {tot} gols')
