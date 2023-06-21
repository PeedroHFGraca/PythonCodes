


                               # Exercício Python #096 - Função que calcula área


def área(largura, comprimento):
    s = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {s}m²')


print('   Controle de Terrenos')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)# <<


                                 # Exercício Python 097 - Um print especial

# Adaptando print ao tamanho da mensagem
def escrever(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


escrever('Curso em vídeo')
escrever('Guanabara')
escrever('Youtube.com')


                                 # Exercício Python 098 - Função de Contador

from time import sleep


def lin(i, f, p):
    if p < 0: # para contar em Negativo
        p *= -1
    if p == 0: # 'contar de 0 em 0' não funciona, logo transformo o Passo 0 em 1
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(1)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.4)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.4)
            cont -= p
        print('FIM!')


lin(1, 10, 1) # 1 = Início,  10 = Fim,  1 = Passo
lin(10, 0, 2) # 10 = Início,  0 = Fim,  2 = Passo
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:     '))
pas = int(input('Passo:   '))
lin(ini, fim, pas)



                               # Exercício Python 099 - Função que descobre o maior
from time import sleep


def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado foi {maior}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

# outra solução

from time import sleep


def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        sleep(0.3)
        print(f'{valor} ', end='')
    if len(num) > 0:
        print(f'Foram informados {len(num)} valores.')
        print(f'O maior valor informado foi {max(num)}')
    else:
        print('Não foi informado nenhum valor.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


                               # Exercício Python  100 - Funções para sortear e somar

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.2)
    print('Pronto!')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor

    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = list()
somapar(numeros)
sorteia(numeros)
