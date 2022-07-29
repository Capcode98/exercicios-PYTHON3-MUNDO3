def area(x, y):
    return f"A área de um terreno de {x} x {y} é de {x * y} m²"


largura = float(input('digite o valor da largura do terreno (m): '))
comprimento = float(input('digite o valor da comprimento do terreno (m): '))

print(area(largura, comprimento))
