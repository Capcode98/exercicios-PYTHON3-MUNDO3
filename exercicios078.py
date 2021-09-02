l = []

while True:
    while True:
        a = int(str(input('quantos numeros voce quer cadestrar?')).strip())
        if type(a) == int:
            break

    for c in range(1, a + 1):
        l.append(int(input('digite os numeros a serem cadastrados: ')))

    break
# maior
n1 = 0
#  menor
n2 = 0
# contador
c = 0
p1 = []
p2 = []
for v in l:
    if c == 0:
        n1 = v
        n2 = v
        c = 1
    if v >= n1:
        n1 = v
    if v <= n2:
        n2 = v
for y, z in enumerate(l):
    if z == n1:
        p1.append(y+1)
    if z == n2:
        p2.append(y+1)
while True:
    print(f'o maior numero digitado foi {n1} na posiçao: ',end='')
    for a in p1:
        print(f'{a}')
    print(f'o menor numero digitado foi {n2} na posiçao: ', end='')
    for b in p2:
        print(f'{b}')
    break
