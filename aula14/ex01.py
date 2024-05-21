cabeca = int(input('digite o total de cabeças: '))
pes = int(input('digite o total de pes: '))

soma_pes= int(cabeca*3+3)
coelhos =int((pes - 2* cabeca)/2)
patos = int(cabeca - coelhos)

print(f'o numero de coelhos é: {coelhos}')
print(f'o numero de patos é: {patos}')

