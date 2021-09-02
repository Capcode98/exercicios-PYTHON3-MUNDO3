a = []
c = 0
while True:
    r = int(str(input('digite um numero:')).strip())

    if c == 0:
        a.append(r)
        c += 1

    else:
        for pos, numero in enumerate(a):

            if r < numero:
                a.insert(pos, r)

                break

            elif r > a[-1] or r == a[-1]:
                a.append(r)

                break

    while True:
        d = str(input('deseja continuar [S/N]')).strip().upper()

        if d == 'S' or d == 'N':
            break

    if d == 'N':
        break


print(a)
