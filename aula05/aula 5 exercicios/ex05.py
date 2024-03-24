x1= int(input('digite o valor de um ano: '))

if x1 % 4 == 0 and not (x1 % 100 == 0 and x1 % 400 == 0):
    print('é um ano bissexto')
else:
    print('não é bissexto')