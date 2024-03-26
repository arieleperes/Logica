valor= float(input('digite o valor da compra'))


if valor< 1000:
    desconto= valor * 0.1
    desconto_total = valor - desconto
    print('o desconto foi de ', desconto_total)
elif valor< 5000:
    desconto=  valor * 0.2
    desconto_total = valor - desconto
    print('o desconto foi de', desconto_total)
else:
    desconto= valor * 0.3
    desconto_total = valor - desconto
    print('o desconto foi de', desconto_total)

