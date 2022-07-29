def maior(num):
    print('Analizando os valores passados...')
    for c in num:
        print(f'{c}', end=" ")
    print(f' Foram informados {len(num)} valores ao todo.')
    print()
    num.sort(reverse=True)
    print(f'O maior valor informado foi: {num[0]}')


valores = list()
while True:
    valores.append(int(input('digite um valor para ser empacotado: ')))
    while True:
        continua = input('deseja continuar (S/N): ').strip().upper()
        if continua == "S" or continua == "N":
            break
    if continua == "N":
        break
maior(valores)
