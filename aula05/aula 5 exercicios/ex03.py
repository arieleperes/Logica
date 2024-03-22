a= int(input('digite o valor do lado do triangulo: '))
b= int(input('digite o valor do lado do triangulo: '))
c= int(input('digite o valor do lado do triangulo: '))

if ((a+b)< c) or ((b+c)< a) or ((a+c) < b):
    print('isso não é um triangulo')

elif a == c == b:
    print('isso é um triangulo equilátero')

elif (a==b) or (a==c) or (b==c):
    print(' isso é um truiangulo Isóceles')

else:
    print('isso é um triangulo escaleno')
