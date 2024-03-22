nota_1= float(input('digite sua nota aqui'))
nota_2= float(input('digite sua nota aqui'))
media= (nota_1 + nota_2) /2

if media > 9:
    print('nota 1:', nota_1, 'nota 2:', nota_2)
    print('sua média é:', media)
    print('A')
    print('Aprovado')

elif media > 7.5:
    print('nota 1:', nota_1, 'nota 2:', nota_2)
    print('sua média é:', media)
    print('B')
    print('Aprovado')

elif media > 6:
    print('nota 1:', nota_1, 'nota 2:', nota_2)
    print('sua média é:', media)
    print('C')
    print('Aprovado')

elif media > 4:
    print('nota 1:', nota_1, 'nota 2:', nota_2)
    print('sua média é:', media)
    print('D')
    print('Reprovado')

else:
    print('nota 1:', nota_1, 'nota 2:', nota_2)
    print('sua média é:', media)
    print('E')
    print('Reprovado')

