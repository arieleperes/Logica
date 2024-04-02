maior_imc= 0
menor_imc= 100
soma_altura = 0
soma_peso = 0

for i in range (1,6):
    altura = float(input(f'digite sua altura {i}'))
    peso = float(input(f'digite seu peso {i}'))
    imc = peso / (altura * altura)
    if imc > maior_imc:
        maior_imc= imc
    if imc < menor_imc
        menor_imc = imc

    soma_altura = soma_altura + altura
    soma_peso = soma_peso + peso

peso_medio = soma_peso / 5
altura_media = soma_altura / 5


print(f' a altura media é {altura_media} e o peso medio é {peso_medio} e o imc menor é {menor_imc} e o maior é {maior_imc}')
