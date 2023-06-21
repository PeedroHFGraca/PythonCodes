from ex108 import moeda # Ou from moeda import aumentar, dobro..

p = float(input('Digíte o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}') # 1ª Moeda = Módulo, 2ª função
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10)),}') # 10 é a 'taxa %' que do ex. Pode alterar
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}',)  # 13 é a 'taxa %' que do ex. Pode alterar
