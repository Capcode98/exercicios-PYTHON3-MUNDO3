print('----> ortografia de numeros por extenço <----')
a = ('zero', 'um', 'dois', 'tres', 'quatro',
     'cinco', 'seis', 'sete', 'oito', 'nove',
     'dez', 'onze', 'doze', 'treze', 'quatorze',
     'quinze', 'dezesseis', 'dezessete', 'dezoito',
     'dezenove', 'vinte')
b = ('0', '1', '2', '3', '4',
     '5', '6', '7', '8', '9',
     '10', '11', '12', '13',
     '14', '15', '16', '17',
     '18', '19', '20')
while True:
    r = int(str(input('digite um numero de 0 a 20 para qual voçe deseja saber a escrita por extenço')).strip())
    k = str(r)
    if k in b:
        break
print(f'o numero {r} escrito por extenço e {a[r]}')
