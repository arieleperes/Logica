valor = input('digite um valor: ')

soma = 0
for letra in valor:
    n = int(letra)
    soma += n
print(f'soma dos números:{soma}')


mult = 1
for letra in valor:
    if int(letra) == 0:
        continue
    n = int(letra)
    mult *= n

print(f'multiplicação dos números: {mult}')

3011392413018