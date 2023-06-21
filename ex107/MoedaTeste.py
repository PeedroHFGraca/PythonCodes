from ex107 import moeda # Ou from moeda import aumentar, dobro..

p = float(input('Digíte o preço: R$'))
print(f'A metade de R${p} é {moeda.metade(p)}')
print(f'O dobro de R${p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10),}') # 10 é a 'taxa %' que do ex. Pode alterar
print(f'Reduzindo 13%, temos R${moeda.dimunuir(p, 13)}',)  # 13 é a 'taxa %' que do ex. Pode alterar
