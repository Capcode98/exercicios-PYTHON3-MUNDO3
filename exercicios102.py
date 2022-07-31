def factorial(number=1, show=False):
    """
    :param number: number to do a calculating factorial
    :param show: show the calculation process
    :return: not return anything
    """

    num_factorial = 1

    if show is True:

        print(f'O fatorial de {number} é : ', end='')

        for c in range(number, 0, -1):

            num_factorial *= c

            if c == 1:

                print(f'{c} = {num_factorial}')

                break

            print(f'{c} x', end=" ")

    else:

        for c in range(number, 0, -1):

            num_factorial *= c

        print(f'O fatorial de {number} é {num_factorial}')


while True:

    number_1 = input('digite um valor para ser calculado o fatorial dele: ')

    if number_1.isnumeric() is True:
        break

while True:

    show_1 = input('Deseja ver o processo de cálculo do fatorial do valor informado? (S/N): ').strip().upper()

    if show_1 == "N" or show_1 == "S":
        break


if show_1 == "S":

    factorial(int(number_1), show=True)

elif show_1 == "N":

    factorial(int(number_1))
