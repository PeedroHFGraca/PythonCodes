

                          # Exercício Python  084 - Lista composta e análise de dados

temp = []
lista = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-='*30)
print(f'Ao todo foram cadastradas {len(lista)} pessoas')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}] ', end ='')
print()
print(f'O menor peso foi de {menor:.1f}Kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()





                              # Exercício Python 085 - Listas com pares e ímpares


n = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'{c}º valor: '))
    if valor % 2 == 0:
        n[0].append(valor)
    else:
        n[1].append(valor)
print('-='*10)
# n[0].sort()  /  ordenar
# n[1].sort()
print(f"Os valores pares digítados foram {sorted(n[0])}")
print(f'Os valores ímpares digítados foram {sorted(n[1])}')





                                        # Exercício Python  086 - Matriz em Python

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):# Linha
    for c in range(0,3):# Coluna
        matriz[l][c] = int(input(f'Digíte um valor para [{l}, {c}]: '))
print('-='*15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz [l][c]:^5}]', end='')
    print()




                                 # Exercício Python 087 - Mais sobre Matriz em Python


matriz = [[0,0,0], [0,0,0], [0,0,0]]
somapar = maior = somacoluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Dígite um valor para [{l}, {c}]: '))
print('-='*15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print(f'A soma dos valores pares é {somapar}')
for l in range(0, 3):
    somacoluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somacoluna}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}') # ou {max(matriz[1])} para pegar o maior valor




                            # Exercício Python 088 - Palpites para a Mega Sena

from time import sleep
from random import randint
lista = list()
jogos = list()
print('-'*30)
print('    JOGA NA MEGA SENA    ')
print('-'*30)
quant = int(input('Quantos jogos quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='* 3, f'SORTEANDO {quant} JOGOS', '-='* 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='* 5, '< BOA SORTE! >', '-=' * 5)




                              # Exercício Python 089 - Boletim com listas compostas
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input('Deseja continuar?[S/N] '))
    if r in 'Nn':
        break
print('-='*20)
print(f'{"Nº":<4}{"nome":<10}{"média":>8}')
print('-='*20)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-='*20)
    opc = int(input('Mostrar as notas de qual aluno?(999 - Parar programa) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'As notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('---- VOLTE SEMPRE ----')
