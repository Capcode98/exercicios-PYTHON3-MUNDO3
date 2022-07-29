def escreva(text):
    n = len(text)
    return print("=" * (n + 2)), print(f' {text} '), print("=" * (n + 2))


texto = input("digite a frase a ser impressa: ").lstrip().rstrip()

escreva(texto)
