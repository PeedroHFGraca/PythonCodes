# LISTA [], Mutável - Diferente das Tuplas
num = [2,5,9,1]
num[2] = 3 # para alterar uma variável declarada
num.append(7) # para adicionar valores a lista
num.sort() # colocar em ordem
num.sort(reverse=True) # inverter ordem
num.insert(2, 0) # inserir na posição dois o numero 0
num.pop() # eleminar variável na última posição
num.remove(1) # remover numero 1
if 5 in num:
    num.remove(5)
else:
    print('Não achei este número')
print(f'Essa lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')

# list() = []
valores = list()
for cont in range(0, 3):
    valores.append(int(input('Digíte um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c+1} encontrei o valor {v}')


a = [2, 3, 4, 7]
b = a
b[2] = 8
# irá alterar as duas listas, pois estão ligadas
print(f'Lista A:{a}')
print(f'Lista B:{b}')

a = [2, 3, 4, 7]
b = a[:] # cópia
b[2] = 8
# criará uma cópia da lista A, alterando só a lista B



