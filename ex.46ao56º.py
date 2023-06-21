# EXCERCÍCIO 46 # FOGOS DE ARTIFÍCIO

from time import sleep
import pygame
print('A queima de fogos de artifício começará em... ')
for c in range(10, -1, -1):  # contagem 1 em 1, de 10 a 0, por isso o -1 no final
    sleep(1)
    print(c)
print('Bommm! Bommm! Piiu-piiu, Bomm!')
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('fogos.mp3')
pygame.mixer.music.play()
pygame.event.wait()




# EXCERCÍCIO 47 # Contagem de pares

for n in range(2, 51, 2):  # mostrar apenas numeros pares de 2 a 51, contando de 2 EM 2
    print(n, end=' ')
print('Acabou.')



# EXCERCÍCIO 48 #Contagem de ímpares

soma = 0  # para somar todos os número digítados
cont = 0 # contador
for c in range(1, 501, 2):  # mostrar apenas numeros ímpares de 1 a 501, contando de 2 EM 2
    soma += c  # para somar todos os número digítados
    cont += 1
print('A soma dos {} valores ímpares é igual a = {} '.format(cont, soma))



# EXCERCÍCIO 49 #Tabuada v.2.0

from time import sleep
num = int(input('Digíte um número para ver sua tabuáda:'))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
    sleep(0.5)



# EXCERCÍCIO 48 # Soma de ímpares múltiplos de três

soma = 0  # para somar todos os número digítados
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c  # para somar todos os número digítados
        cont += 1
print('A soma dos {} valores ímpares e multilos de 3 é igual a = {} '.format(cont, soma))



# EXCERCÍCIO 50 # Soma dos pares

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digíte o {}º valor número:'.format(c)))
    if num % 2 == 0:
        cont += 1
        soma += num  # para somar todos os número pares digítados
print('Você informou {}´números PARES e a soma entre eles é igual a = {}'.format(cont, soma))



# EXCERCÍCIO 51 # Progressão Aritmética

print('='*42)
print('\033[7;40m '*9, 'PROGRESSÃO ARITIMÉTICA', '         \033[m'*3)
print('='*42)
primeiro = int(input('\033[1mPrimeiro termo:\033[m'))
razao = int(input('\033[1mRazão:')) #contar de quanto em quanto
decimo = primeiro + (10 - 1) * razao # 10 = quantidade de termos (podendo ser alterada). fórumla para calcular 'enésimo' termo de um PA
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end=' →')
print('FIM.')



# EXCERCÍCIO 52 # Números primos

num = int(input('Digíte um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0: #SE o resto da divisão for = 0
        print('\033[1;33m', end='')
        tot += 1
    else:
        print('\033[;31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO')



# EXCERCÍCIO 53 # Detector de Palíndromo

''' Ex. de PALÍNDROMOS

Apos A Sopa
A Sacada Da Casa
A Torre da Derrota
O lobo Ama o Bolo
Anotaram a Data da Maratona
'''

frase = str(input('Digíte uma frase: ')).strip().upper() #strip corta os espaços antes e depois da frase
palavras = frase.split() #fatia a frase
junto = ''.join(palavras)
# '' = sem espaços / .join = juntar
inverso = ''
''' ALTERNATIVA PARA NÃO UTILIZAR FOR
inverso = junto[::-1] / : não define começo, : não define fim, -1 contar de trás para frente
'''
for letra in range(len(junto)-1, -1, -1): # vai contando ao contrário de 1 em 1
    inverso += junto[letra]
print(junto,' ↔  ', inverso)
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO')
else:
    print('A frase digítada não é um PALÍNDROMO')



# EXCERCÍCIO 54 # Grupo da Maioridade

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nasc = int(input('Digíte o ano em que a {}º pessoa nasceu:'.format(pessoas)))
    if atual - nasc >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo temos {} pessoas maiores de idade \n e {} menores.'.format(totmaior, totmenor))



# EXCERCÍCIO 55 # Maior e menor da sequência

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digíte o peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg.\nE o menor foi de {}Kg'.format(maior, menor))



# EXCERCÍCIO 56 # Analisador completo

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}º PESSOA -----'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F/]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4 # Para calcular a media somaremos todas as idades e dividiremos pela quantidade de pessoas(4)
print('A média de idade do grupo de é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('{} mulheres tem menos de 20 anos'.format(totmulher20))