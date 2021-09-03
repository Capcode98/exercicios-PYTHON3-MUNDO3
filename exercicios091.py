from random import randint
from time import sleep
from operator import itemgetter
jogadas = dict()
ranking = list()

for c in range(1, 5):
    jogadas[f'Jogador {c}'] = randint(1, 6)
    sleep(1)
    print(jogadas[f'Jogador {c}'])

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

for k, v in enumerate(ranking):
    print(f'o {k+1}º é o {v[0]} e fez {v[1]} pontos')
    sleep(1)

print(f'{jogadas},\n {ranking}')
