v = 0
frase = input('digite uma frase')

for letra in frase:
    if letra.upper() in "AEIOU":
        v = v + 1

print(f'a frase tem {v} vogal(is)')

vogail_a = frase.count('a')
vogail_e = frase.count('e')
vogail_i = frase.count('i')
vogail_o = frase.count('o')
vogail_u = frase.count('u')


print(f'a quantidade de vogais é {vogais}')

