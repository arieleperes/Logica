with open('texto1.txt','r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        linha = arquivo.readline()

usuario = []
espaçosUtilizados = []
espaçoTotal = 0.0

for linha in linha:
    campo = linha.split()
    usuario = campo[0]
    espaçoUtilizado = int(campo[1])
    usuario.append(usuario)
    espaçosUtilizados.append(espaçoUtilizado)
    espaçosUtilizados += espaçoTotal

print('Nr.  Usuario        Espaco utilizado     %% do uso')
for i in range(0, len(usuario)):
    espacoMB = espacoUtilizado[i] / (1024.0 * 1024.0)
    percentualUso = espacosUtilizado[i] / espacoTotal
    perc = percentualUso * 100
    print(f'{i+1:2d} - {usuarios[i]:11s} -  {espacoMB:13.2f} MB   - {perc:7.2f}%')


print(f'\nEspaco total ocupado: {(espacoTotal / (1024.0 * 1024.0)):.2f} MB')
space = (espacoTotal / len(usuarios) / (1024.0 * 1024.0))
print(f'Espaco medio ocupado: {space:.2f} MB')
