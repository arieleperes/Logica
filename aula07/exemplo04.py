
soma = 0
idade = 100
quantidade = 0

while idade != 0:
    idade = int(input(f'entre com a idade {quantidade + 1}'))
    if idade != 0:
        soma = soma + idade
        quantidade = quantidade + 1

media = soma / quantidade
print(f'a media das {quantidade} idades é {media: 5.2f}')


