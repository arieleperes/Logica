nome = input('digite seu nome completo: ')
nascimento = input('digite a data de nascimento <dd/mm/aaaa>')
data = nascimento.split('/')
palavras= nome.split()
pre_nome = palavras[0]
sobrenome = palavras[1]

print(f'olá{pre_nome}..... muito bonito seu sobrenome : {sobrenome}')
print(f'voce nasceu no dia {data[0]} e no mes {1}')