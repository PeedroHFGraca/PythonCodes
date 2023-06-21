
                                #  Exercício Python #072 - Número por Extenso

# minha SOLUÇÃO
'''n = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
while True:
    c = int(input('Digíte um número entre 0 e 20: '))
    while c not in n:
         print('Tente novamente!', end=' ')
         break
    if c in n:
        print(f'Você digítou o número {c}')
'''

n = ('zero', ' um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis',
     ' dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    c = int(input('Digíte um número entre 0 e 20: '))
    if 0 <= c <= 20:
        break
    print('Tente novamente! ', end='')
print(f'Você digitou o número {n[c]}')




                               # Exercício Python #073 - Tuplas com Times de Futebol

from time import sleep
times = ['', 'Botafogo', 'Fortaleza', 'Palmeiras', 'Internacional', 'Fluminesne',
         'Cruzeiro', 'Grêmio', 'São Paualo', 'Vasco Da Gama', 'Atlético-MG',
         'Santos', 'Bragantino', 'Flamengo', 'Atlético-PR', 'Bahia', 'Goiás',
         'Corinthians', 'Cuiabá', 'Coritiba', 'América-MG']

print('\033[1m=\033[m'*43)
print('{:^53}'.format('\033[1;7;40mTabela Brasileirão 2023\033[m'))
print('\033[1m=\033[m'*43)
sleep(1)

print('\n\033[1;4mPrimeiros colocados:\033[m ')
for c in range(1, 6):
    print(f'{c:02}º {times[c]}')
sleep(1)

print('\n\033[1;4mÚltimos colocados:\033[m ')
for c in range(16, 21):
    print(f'{c:02}ª {times[c]}')
sleep(1)

print(f'\nO Time \033[1;4mCorinthians\033[m está na \033[1;4m{times.index("Corinthians")}\033[mº Posição: ')



print('\n\033[1;4mTimes Em Ordem alfabética\033[m')
for c in range(1, 21):
        print((f'\033[1m{c:02}\033[mº {sorted(times[:21])}'))
        sleep(0.4)

# Solução Guanabára
'''
times = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Internacional', 'Fluminesne', 'Cruzeiro', 'Grêmio', 'São Paualo',
'Vasco Da Gama', 'Atlético-MG', 'Santos', 'Bragantino', 'Flamengo', 'Atlético-PR', 'Bahia', 'Goiás', 'Corinthians',
'Cuiabá', 'Coritiba', 'América-MG')
print('-='*15)
print(f'Lista de times Brasileirão: {times}')
print('-='*15)
print(f'Primeiros colocados: {times[:5]}')
print('-='*15)
print(f'Últimos colocados: {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'O Corithians está na {times.index("Corinthians")+1}º posição')
'''



                                # Exercício Python 074 - Maior e menor valores em Tupla

from random import randint
num = randint(1,10), randint(1, 10), randint(1,10), randint(1, 10), randint(1, 10)
print('Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(num)} ')
print(f'E o menor foi {min(num)}')


                                # Exercício Python 075 - Análise de dados em uma Tupla

n = (int(input('Digíte um número: ')),
    int(input('Digíte um número: ')),
    int(input('Digíte um número: ')),
    int(input('Digíte um número: ')))
print(f'Você DIGÍTOU os valores {n}')
print(f'O valor 9 apareceu {n.count(9)}º vezes')
if 3 in n:
    print(f'O valor 3 está na {n.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digítado.')
print('Os valores pares digítados foram:')
for c in n:
    if c % 2 == 0:
        print(c, end='')



                                   # Exercício Python 076 - Lista de preço com Tupla

listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Apontador', 1.50,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Compasso', 7.20,
            'Mochila', 120.32,
            'Canetas', 39.40,
            'Livros', 65.00 )
print('-='*30)
print(f'{"LISTAGEM DE PREÇOS":^60}')
print('-='*30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<40}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-='*30)




                                   #Exercício Python 077 - Contando vogais em Tupla

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra.upper()}', end=' ')