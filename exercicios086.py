matriz = list()
coluna1 = list()
coluna2 = list()
coluna3 = list()
matriz.append(coluna1)
matriz.append(coluna2)
matriz.append(coluna3)

while True:
    coluna1.append(int(str(input('digite um numero para a posiçao [1:1] da matriz:')).strip()))
    coluna2.append(int(str(input('digite um numero para a posiçao [1:2] da matriz:')).strip()))
    coluna3.append(int(str(input('digite um numero para a posiçao [1:3] da matriz:')).strip()))
    coluna1.append(int(str(input('digite um numero para a posiçao [2:1] da matriz:')).strip()))
    coluna2.append(int(str(input('digite um numero para a posiçao [2:2] da matriz:')).strip()))
    coluna3.append(int(str(input('digite um numero para a posiçao [2:3] da matriz:')).strip()))
    coluna1.append(int(str(input('digite um numero para a posiçao [3:1] da matriz:')).strip()))
    coluna2.append(int(str(input('digite um numero para a posiçao [3:2] da matriz:')).strip()))
    coluna3.append(int(str(input('digite um numero para a posiçao [3:3] da matriz:')).strip()))

    print('=' * 45)
    print(f'a matriz digitada foi:\n'
          f'     1°   2°   3°\n'
          f'1° [ {coluna1[0]} ][ {coluna2[0]} ][ {coluna3[0]} ]\n'
          f'2° [ {coluna1[1]} ][ {coluna2[1]} ][ {coluna3[1]} ]\n'
          f'3° [ {coluna1[2]} ][ {coluna2[2]} ][ {coluna3[2]} ]')
    print('=' * 45)

    while True:
        d = str(input('deseja continuar? [S/N]')).strip().upper()
        if d in 'S' or d in 'N':
            break
    if d == 'N':
        break
