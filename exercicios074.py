from random import randint
print('iremos sortear valores e mostrar eles a vcs com algumas informaçoes importantes')

M = 0
m = 10

a = randint(0, 10)
b = randint(0, 10)
c = randint(0, 10)
d = randint(0, 10)
e = randint(0, 10)

t = (a, b, c, d, e)

for i in range(0, 5):
    if t[i] < m:
        m = t[i]
    if t[i] > M:
        M = t[i]

print(f'os valores sorteados foram {t[0]} {t[1]} {t[2]} {t[3]}')
print(f'O maior numero foi {M} e o menor numero foi {m}')
