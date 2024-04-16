salario= float(input('salario atual:'))
aumento= float(input('percentual de aumento:'))


salario_atual= salario + ((aumento * salario)/100)
print(f'salario atual: R${salario:8.2f}')
print(f'aumento......: R${aumento:8.2f}')
print('................................')
print(f'salario_atual: R${salario_atual}')
