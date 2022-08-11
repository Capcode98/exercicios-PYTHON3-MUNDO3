from exercicios107_a_112 import moeda_ex107

p = float(input('Digite o preço: R$ '))
print(f'''A metade de {p} é {moeda_ex107.metade(p)}\n
O Dobro de {p} é {moeda_ex107.dobro(p)}\n
Aumentando 10% o {p}, temos {moeda_ex107.aumentar(p, 10)}\n
Reduzindo 13% o {p}, temos {moeda_ex107.diminuir(p, 13)}\n
''')
