                                  #Exercício Python #057 - Validação de Dados


sexo = str(input('Informe seu sexo[F/M]: ')).strip().upper()[0] #pegar só a primeira letra da frase
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))



                               #Exercício Python #058 - Jogo da Adivinhação v2.0


from random import randint
computador = randint(0, 10)
print('Sou seu computador. \nVou pensar em número de 0 a 10. \nConsegue adivinhar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    elif jogador < computador:
        print('Mais... Tente de novo!')
    else:
        print('Menos...Tente de novo!')
print('Acertou com {} tentativas. Parábens!'.format(palpites))



                            #Exercício Python 059 - Criando um Menu de Opções

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''       [ 1 ] Somar
       [ 2 ] Multiplicar
       [ 3 ] Maior número
       [ 4 ] Novos números
       [ 5 ] Finalizar
    ''')
    print('-=-'*20)
    opção = int(input('Sua opção: '))
    if opção == 1:
        tot = n1 + n2
        print('A soma entre {} e {} é = {}'.format(n1, n2, tot))
    elif opção == 2:
        tot = n1 * n2
        print('{} x {} = {}'.format(n1, n2, tot))
    elif opção == 3:
        if n1 < n2:
            maior = n2
        else:
            maior = n1
        print('Entre {} e {}, o maior é {}'.format(n1, n2, maior))
        if n1 == n2:
            print('Os valores {} e {} são iguais'.format(n1, n2))
    elif opção == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando ...')
    else:
        print('Opção inválida. Tente novamente!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    print('-=-' * 20)
    sleep(0.7)
print('FIM do programa. Volte sempre!')



                                #Exercício Python #060 - Cálculo do Fatorial
# Resolvendo com biblioteca:
from math import factorial
n = int(input('Digíte um número para ver seu cálculo fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))

# Modo tradicional:
n = int(input('Digíte um número para ver seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '=', end='')
    f *= c
    c -= 1
print(' {} '.format(f))

# Resolvendo com For:
n = int(input('Digíte um número para ver seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
for c in range(5, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))



                          #Exercício Python # 061 - Progressão Aritmética v2.0

#Continuação do ex 51
print('-=-' * 10)
print('       Gerador de PA')
print('-=-' * 10)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = p
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += r
    cont += 1
print('FIM.')



                        #Exercício Python # 062 - Super Progressão Aritmética v3.0

from time import sleep
print('-=-' * 10)
print('       Gerador de PA')
print('-=-' * 10)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Deseja mostar quantos termos a mais? '))
print('Finalizando...')
sleep(1)
print('Progressão finalizada com {} termos.'.format(total))


                         #Exercício Python  # 063 - Sequência de Fibonacci v1.0

#Sequencia fibonacci = 0 → 1 → 1 → 2 → 3 → 5 → 8 (somar os dois primeiros termos para obeter o próx.)
print('-'*30)
print('     \033[1;4;29mSequência Fibonacci\033[m')
print('-'*30)
n = int(input('Quantos termos você deseja mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
print('~'*30)



                        # Exercício Python 064 - Tratando vários valores v1.0

# n = 0 , c = 0 , soma = 0 - simplificando ...
n = c = soma = 0
n = int(input('Digíte o valor 999 para finalizar o programa:'))
while n != 999:
    c += 1
    soma += n
    n = int(input('Digíte o valor 999 para finalizar o programa:'))
print('Você digitou {} números, e a soma entre eles foi {}'.format(c, soma))
print('FIM')



                          #Exercício Python  #065 - Maior e Menor valores

r = 'S'
soma = quant = média = maior = menor = 0
while r in 'Ss':
    num = int(input('Digíte um valor:'))
    soma += num
    quant += 1
    if quant == 1:
         maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    r = str(input('Deseja continuar?[S/N]  ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} número(s) e a média foi {}'.format(quant, média))
print('O maior valor digitado é {} e o menor {}'.format(maior, menor))
