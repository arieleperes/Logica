n = int(input(f'digite um numero:'))
e= 0
k = 1

while k <= n:
     e = e + 2**k
     k = k + 1

print(f'valor de E= {e}')
