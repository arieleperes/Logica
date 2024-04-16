lista = []

for i in range(5):
    v = int(input(f'digite 5 numeros inteiros {i+1}: '))
    lista.append(v)

maior = max(lista)
p= lista.index(maior)

print (p)