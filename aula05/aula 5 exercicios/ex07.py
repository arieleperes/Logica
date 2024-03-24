litros= float(input('quantidade de litros: '))
tipo= (input('tipo de combustivel: '))

desconto = 0

if tipo == 'A':
    if litros <= 20:
        desconto= 0.03
    else:
        desconto= 0.05

    valor_total= litros * 1.90
    valor_pagar= valor_total - ( valor_total * desconto)

    print(' o valor a pagar é:', valor_pagar)

elif tipo == 'G':
    if litros <= 20:
        desconto= 0.04
    else:
        desconto= 0.06

    valor_total= litros * 2.50
    valor_pagar= valor_total - ( valor_total * desconto)

    print(' o valor a pagar é: ', valor_pagar)

else:
    print('erro')

