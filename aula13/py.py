def exibir_menu():
    print('Menu')
    print('1 - Cadastrar')
    print('2 - Exibir Frase')
    print('3 - Sair')

while True:
    exibir_menu()
    opcao = input('Escolha uma opção do menu: ')

    if opcao == '1':
        print('funcao cadastrar')
    elif opcao == '2':
        print('funcao exibir frase')
    elif opcao == '3':
        break
    else:
        exibir_menu()

print("bye!")


