def epar(n):
    if n % 2 == 0:
        return True

x = int(input('digite um valor: '))

if epar(x):
    print('o valor é par')
else:
    print('o valor é impar')