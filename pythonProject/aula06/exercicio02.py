valor= float(input('digite o valor da compra'))


if valor< 1000:
    desconto= valor * 0.1
    print('o desconto foi de ', desconto)
elif valor< 5000:
    desconto=  valor * 0.2
    print('o desconto foi de', desconto)
else:
    desconto= valor * 0.3
    print('o desconto foi de', desconto)