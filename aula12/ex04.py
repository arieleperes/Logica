from math import pow
def potencia(numero,expoente = 2):
    resultado = pow(numero, expoente)
    return resultado

n = float(input('digite um numero: '))
e = int(input('expoente: '))


print(f'valor com expoente: {potencia(n,e)}')
print(f'valor sem expoente: {potencia(n)}')