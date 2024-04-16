frase = input('digite uma frase: ')

palavras = frase.split()
frase1 = ''
for palavra in palavras:
    frase1 = frase + palavra
frase2 = frase1[::-1]
if frase1 == frase2:
    palindrono = True
else:
    palindrono = False
if palindrono:
    print('é um palindromo')
else:
    print('não é um palindromo!')










while True:

    frase = input('digite uma frase: ').strip()
    frase.split()
    if not frase.isalpha():
        print(frase[::-1])
        break
    else:
        print('não é uma frase')




