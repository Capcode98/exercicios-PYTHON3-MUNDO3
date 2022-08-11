from exercicios107_a_112 import moeda_ex108

p = float(input('Digite o preço: R$ '))
print(f'''A metade de {moeda_ex108.moeda(p)} é {moeda_ex108.moeda(moeda_ex108.metade(p))}\n
O Dobro de {moeda_ex108.moeda(p)} é {moeda_ex108.moeda(moeda_ex108.dobro(p))}\n
Aumentando 10% o {moeda_ex108.moeda(p)}, temos {moeda_ex108.moeda(moeda_ex108.aumentar(p, 10))}\n
Reduzindo 13% o {moeda_ex108.moeda(p)}, temos {moeda_ex108.moeda(moeda_ex108.diminuir(p, 13))}\n
''')
