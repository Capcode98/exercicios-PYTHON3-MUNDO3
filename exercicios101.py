from datetime import date


def voto(ano):
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return print("NÃO VOTA")
    elif 16 <= idade < 18:
        return print("OPCIONAL")
    elif 18 <= idade <= 65:
        return print("OBRIGATÓRIO")
    elif 65 < idade:
        return print("OPCIONAL")


r = int(input('digite o seu ano de nascimento (ex: AAAA): '))
voto(r)
