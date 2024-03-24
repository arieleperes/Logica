numero = int(input('digite um numero menor que 1000'))

if numero >= 1000:
    print('numero invalido')

else:
    centena= numero // 100
    dezena= numero % 100 // 10
    unidade= numero - centena * 100 - dezena * 10

    print(centena,dezena,unidade)

    saida= ''
    if centena > 0:
        if centena > 1:
            saida += f'{centena} centenas'
        else:
            saida += f'{centena} centena'

    if dezena > 0:
        if saida != '':
            saida += ', '
        if dezena > 1:
            saida += f'{dezena} dezenas'
        else:
            saida += f'{dezena} dezena'

    if unidade > 0:
        if saida != '':
            saida += ' e '
        if unidade > 1 :
            saida += f'{unidade} unidades'
        else:
            saida += f'{unidade} unidade'

    print(saida)


