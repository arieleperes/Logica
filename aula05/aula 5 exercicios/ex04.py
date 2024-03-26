a = float(input('digite o valor de A: '))

if a == 0:
    print('não é uma equação de segundo grau ')

else:
    b = float(input('digite o valor de B: '))
    c = float(input('digite o valor de C: '))

    delta= b**2 - 4 * a * c

    if  delta == 0:
        print('a equação possui apenas uma raiz',)
        x= -b / 2 * a 