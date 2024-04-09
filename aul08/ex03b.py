v = 0
frase = input('digite uma frase').upper()

for vogal in 'AEIOU':
    v = v + frase.count(vogal)


print(f'a frase tem {v} vogal(is)')