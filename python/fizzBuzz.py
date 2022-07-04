# FizzBuzz
#
# Dado um inteiro n, para cada valor inteiro i entre 1 e n incluso,
# imprima um valor por linha conforme a seguinte especificação:
#
# - Se n é divisível por 3 e 5, substitua por “FizzBuzz”.
# - Se n é divisível por 3, substitua por “Fizz”.
# - Se n é divisível por 5, substitua por “Buzz”.
# - Se n não é divisível nem por 3 nem por 5, apenas é dito n.


# Entrada: inteiro n (0 < n< 2*10^5)

def fizzBuzz(value):

    if value % 3 == 0 and value % 5 == 0:
        print("FizzBuzz")
    elif value % 3 == 0 and value % 5 != 0:
        print("Fizz")
    elif value % 3 != 0 and value % 5 == 0:
        print("Buzz")
    else:
        print(value)


if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1, 1):
        fizzBuzz(i)
