a = int(str(input('digite o 1º numero:')).strip())
b = int(str(input('digite o 2º numero:')).strip())
c = int(str(input('digite o 3º numero:')).strip())
d = int(str(input('digite o 4º numero:')).strip())

t = (a, b, c, d)

k = 0

for i in range(0, len(t)):
    if t[i] == 3:
        print(f'o primeiro numero 3 esta na posiçao: {t.index(3) + 1}')
        k = 1
        break

if k == 0:
    print(f'nao foi digitado o valor 3')

print(f'a quantidade de numeros 9 e: {t.count(9)}')
print(f'os numeros pares sao:')

z = 0

for i in range(0, len(t)):
    if t[i] % 2 == 0:
        z = 1
        print(t[i])

if z == 0:
    print('''    ops...
    desculpe mas...
    nao teve nenhum numero par...''')
