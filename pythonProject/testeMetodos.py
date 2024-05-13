filmes = {
    'avatar':2009,
    'titanic':1997,
    'starwarts':2015,
    'harry-potter':2011,
    'avangers':2012
}

# filmes_novachave = filmes.fromkeys(filmes)
#print(filmes_novachave)
#filmes_novachave = filmes.fromkeys(filmes, 'bilionario')
#print(filmes_novachave)

#get
#print(filmes.get('avatar'))
#print(filmes)

#items
#for chave, valor in filmes.items():
   # print(f'assiste a {chave.upper()} lançado em {valor}!')

# keys
#print(filmes.keys())
# values
#print(filmes.values())

#update
filmes.update({"frozen":2013})
print(filmes)