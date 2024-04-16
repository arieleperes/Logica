while True:
    idade = input('digite sua idade: ')
    idade.strip()
    if idade.isdigit():
        idade = int(idade)
        break
    else:
        print ('apenas numeros')


