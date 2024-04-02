ano_nascimento= int(input('ano de nascimento'))
ano_atual= int(input('ano atual'))

qtd_anos= ano_atual - ano_nascimento
meses= qtd_anos* 12
semanas=qtd_anos*52
dias= qtd_anos* 365

print('voce tem', qtd_anos,'anos')
print('voce tem', meses,'meses')
print('voce tem',semanas,'semanas')
print('voce tem',dias, 'dias')


