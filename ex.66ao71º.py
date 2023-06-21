                                 #Exercício Python # 066 - Vários números com flag

s = t = 0
while True:
    n = int(input('Digíte um número (999 para parar): '))
    if n == 999:
        break
    s += n
    t += 1
print(f'Ao todo foram digítados {t} números.\nA soma entre eles é = {s}')



                                      #Exercício Python # 067 - Tabuada v3.0
c = 0
while True:
    n = int(input('Digíte um número para ver sua tabuada: '))
    print('-'*40)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {c*n}')
    print('-' * 40)
print('Programa finalizado. Volte sempre!')




                                   # Exercício Python 068 - Jogo do Par ou Ímpar

from random import randint
v = 0
print('=-=' *10)
print('Vamos jogar PAR ou ÍMPAR!')
print('=-=' *10)
while True:
    jogador = int(input('Digíte um valor: '))
    computador = randint(1, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar:[P/I] ')).strip().upper()[0]
    print('-'*30)
    print(f'Você jogou {jogador} e o computador {computador}. O total é de = {total}. ', end='')
    print(f'DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!!!')
            v += 1
        else:
            print('Você perdeu! \nGAME OVER! ', end='')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!!!')
            v += 1
        else:
            print('Você perdeu! \nGAME OVER! ', end='')
            break
    print('Vamos jogar novamente...!')
    print('-' * 30)
print(f'Você venceu {v} vezes')




                                  #Exercício Python  #069 - Análise de dados do grupo


print('=-='*9, 'CADASTRE UMA PESSOA', '=-='*9)
maioridade = totm20 = homem = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    r = ' '
    while r not in 'SN':
        print('-=-' * 10)
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print('-=-' * 10)
    if r == 'N':
        break
print(f'Total de pessoas maiores de 18 anos: {maioridade} ')
print(f'Ao todo temos {homem} homens cadastrado(s)')
print(f'E temos {totm20} mulheres com menos de 20 anos')




                            #Exercício Python #070 - Estatísticas em produtos

tot = totmil = totmenor = c = 0
barato = ' '
print('='*10, 'SUPER LOJA BARATÃO', '='*10)
while True:
    produto = str(input('Digíte o nome do produto desejado: '))
    preço = int(input('Valor do produto: R$'))
    tot += preço
    c += 1
    if preço > 1000:
        totmil += 1
    if c == 1 or preço < totmenor:
        menor = produto
        totmenor = preço
        barato = produto
    r = ' '
    while r not in 'SN':
        print('-' *40)
        r = str(input('Deseja continuar comprando?[S/N] ')).strip().upper()[0]
        print('-' *40)
    if r == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R${tot:5.2f}')
print(f'Temos {totmil} produto(s) custando mais de R$1000.')
print(f'E o produto mais barato foi {barato} que custou {totmenor:.2f}')



                                #Exercício Python 071 - Simulador de Caixa Eletrônico


print('='*40)
print('{:^40}'.format('BANCO CEV'))
print('='*40)
valor = int(input('Dígíte o valor que deseja sacar: R$'))
tot = valor
céd = 50
totcéd = 0
while True:
    if tot >= céd:
        tot -= céd
        totcéd += 1
    else:
        if totcéd > 0:
           print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd =1
        totcéd = 0
        if tot == 0:
            break
print('='*40)
print('{:^40}'.format('BANCO CEV - Volte sempre!'))
