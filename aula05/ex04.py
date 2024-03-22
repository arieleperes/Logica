a= input("valor do lado do triangulo: ")
b= input("valor do lado do triangulo: ")
c= input("valor do lado do triangulo: ")

if ((a+b)<c) or ((b+c)<a) or ((c+a)<b):
    print('não é um triangulo')

elif a == b == c:
    print('é um triangulo equilatero')

elif (a==b) or (a==c) or (b==a) or (b==c):
    print('é um triangulo isosceles')
else:
    print('isso é um triangulo escaleno')