                               # Exercício Python #078 - Maior e Menor valores na Lista

# Solução Guanabára
'''
valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digíte um valor para posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('-='*30)
print(f'Você digítou os valroes {valores}')
print(f'O maior valor digítado foi {max(valores)} na posição ', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digítado foi {min(valores)} na posição ', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ')
'''

lista = []
maior = []
menor = []
for c in range(0, 5):
    lista.append(int(input('Digíte um valor: ')))
for p, v in enumerate(lista):
    if v == max(lista):
        maior.append(p)
    if v == min(lista):
        menor.append(p)
print(f'Você DIGÍTOU OS VALORES {lista}')
print(f'O maior valor foi {max(lista)}, na posição: {maior}')
print(f'O menor valor foi {min(lista)} na posição: {menor}')





                               # Exercício Python 079 - Valores únicos em uma Lista

num = []
while True:
    n = int(input('Digíte um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
         print('Valor duplicado! Não adicinado.')
    print('-='*30)
    r = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    print('-=' * 30)
    if r == 'N':
        break
num.sort()
print(f'Os valores adicionados foram {num}')




                               # Exercício Python  080 - Lista ordenada sem repetições

# Colocando em ordem sem o insort
lista = []
for c in range(0, 5):
    n = int(input('Digíte um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
             if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
             pos += 1
print('-='*30)
print(f'Os valores digítados em ordem foram {lista}')




                                 # Exercício Python  081 - Extraindo dados de uma Lista

lista = []
while True:
    n = int(input('Digíte um valor: '))
    lista.append(n)
    print('-'*22)
    r = str(input('Deseja continuar?[S/N]')).strip()
    print('-' * 22)
    if r in 'Nn':
        break
lista.sort(reverse=True)
print(f'Essa lista possuí {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')





                              #Exercício Python  082 - Dividindo valores em várias listas


lista = []
pares = []
ímpares = []
while True:
    n = int(input('Digíte um valor: '))
    lista.append(n)
    r = str(input('Deseja continuar?[S/N] ')).strip()
    if r in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
lista.sort()
pares.sort()
ímpares.sort()
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')




                            # Exercício Python 083 - Validando expressões matemáticas

expressão = str(input('Digíte uma expressão matemática com parenteses: '))
pilha = []
for símbolo in expressão:
    if símbolo == '(':
        pilha.append('(')
    elif símbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está inválida!')
