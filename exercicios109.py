from exercicios107_a_112 import moeda_ex109

p = float(input('Digite o preço: R$ '))
print(f'''A metade de {moeda_ex109.moeda(p)} é {moeda_ex109.metade(p)}\n
O Dobro de {moeda_ex109.moeda(p)} é {moeda_ex109.dobro(p)}\n
Aumentando 10% o {moeda_ex109.moeda(p)}, temos {moeda_ex109.aumentar(p, 10)}\n
Reduzindo 13% o {moeda_ex109.moeda(p)}, temos {moeda_ex109.diminuir(p, 13)}\n
''')
