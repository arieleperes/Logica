frase= input('digite uma frase: ')

quantidade= 0
for caracter in frase:
    if caracter in 'aeiouAEIOU':
        quantidade = quantidade + 1

print(f'existem {quantidade} vogais ')


