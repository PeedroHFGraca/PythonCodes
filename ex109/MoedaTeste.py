from ex109 import moeda # Ou from moeda import aumentar, dobro..

p = float(input('Digíte o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}') # 1.ª Moeda = Módulo, 2.ª função
print(f'O dobro de  {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}') # 10 é a 'taxa %' que do ex. Pode alterar
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')  # 13 é a 'taxa %' que do ex. Pode alterar
