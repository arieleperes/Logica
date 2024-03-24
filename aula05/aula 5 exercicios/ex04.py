import math

a = float(input('digite o valor de A: '))

if a == 0:
    print('não é uma equação de segundo grau ')

else:
    b = float(input('digite o valor de B: '))
    c = float(input('digite o valor de C: '))

    delta= b ** 2 - 4 * a * c

    if delta < 0:
        print('não tem raiz real')
    elif delta == 0:
        raiz= math.sqrt(delta)
        print ('a raiz é', raiz)
    else:
        raiz= math.sqrt(delta)
        print('as raizes são:',raiz,' e ',-raiz)