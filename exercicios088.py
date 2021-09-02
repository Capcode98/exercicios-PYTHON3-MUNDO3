from random import randint
import time
jogo = list()
jogos = list()

p = int(str(input('digite a quantidade de jogos voçe quer fazer de uma unica vez:')).strip())

print(f'\na quantidade de jogos pedidas foram: {p} \n')
while len(jogos) != p:
    while len(jogo) != 6:
        y = randint(1, 60)
        if y not in jogo:
            jogo.append(y)

    if len(jogo) == 6:
        jogo.sort()
        jogos.append(jogo[:])
        print(f'o jogo {len(jogos)}º e : {jogo}')
        time.sleep(1)
        del jogo
        jogo = list()
time.sleep(1)
print(f'os jogos criados foram: {jogos}')
