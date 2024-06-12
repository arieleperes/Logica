with open('frutas.txt','a', encoding='utf-8')as arquivos:
    while True:
        fruta = input('digite o nome de uma fruta: ')
        if fruta == 'sair':
            break
        else:
            arquivos.write(fruta)
            arquivos.write('\n')