
 #Aula 12 - Exercício 36 - Empréstimo Bancário.

imovel = float(input('Valor do imóvel desejado: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestaçao = imovel / (anos * 12)
minimo = salario * 30/100
if prestaçao <= minimo:
    print('o Empréstimo \033[4;32mPODE\033[m ser concedido!!!')
else:
    print('O Empréstimo \033[4;31mNÃO\033[m pode ser concedido.')
print('Para pagar um imóvel de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(imovel, anos, prestaçao))


   # Aula 12 - Exercício 37 - Conversor de Bases Numéricas

num = int(input('Digíte um número inteiro:'))
print('''Escolha uma das bases para conversão:
\033[1;36m[ 1 ]\033[m Converter para \033[1;36mBinário\033[m:
\033[1;33m[ 2 ]\033[m Converter para \033[1;33mOctal\033[m:
\033[1;35m[ 3 ]\033[m Converter para \033[1;35mHexadecimal\033[m:
''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
# 0b = Binário / 0o = Octal / Hexadecimal 0x (NÃO IMPORTA APARECER ESSES CONCEITOS, POR ISSO [2:] = contar a partir
# da terceira letra.




   # Aula 12 - Exercício 38 - Comparando números

n1 = float(input('Primeiro valor:'))
n2 = float(input('Segundo valor:'))
if n1 > n2:
    maior = n1
    print('O primeiro valor ({}) é maior'.format(n1))
elif n1 < n2:
    maior = n2
    print('O segundo valor ({}) é maior'.format(n2))
else:
    print('Os valores são iguais')

''' maior = 0
    menor = 0
    for c in range(1, 4):
        a = int(input(('{}º valor:'.format(c))))
        if c == 1:
            maior = a
            menor = a
        else:
            if a > maior:
                maior = a
            if a < menor:
                menor = a
    print('O maior valor é {} \nE o menor {}'.format(maior, menor))
'''



 # Exercício Python 039 - Alistamento Militar

from datetime import date
print('\033[1;35m-\033[m'*60)
print('\033[1;4;30;41m               ALISTAMENTO MILITAR OBRIGATÓRIO              \033[m')
print('''Sexo:
[ 1 ] FEMININO
[ 2 ] MASCULINO
''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('Alistamento NÃO obrigatório.\nEm caso de alistamento voluntário, entre em contato pelos nossos canais de '
          'atendimento.')
elif opção != 2:
    print('Opção inválida!')
else:
 nascimento = int(input('Ano de nascimento:'))
 idade = date.today().year - nascimento
 print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, date.today().year))
 if idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} ano(s) '.format(saldo))
    print('Seu alistamento foi em {}'.format(date.today().year - saldo))
 elif idade < 18:
    saldo = 18 - idade
    ano = nascimento + saldo + idade
    print('Faltam {} ano(s) para seu alistamento, que será em {}'.format(saldo, ano))
 else:
    print('Você deve se alistar \033[1;31mIMEDIATAMENTE\033[m !')



 #Exercício Python 040 - Aquele clássico da Média

nota1 = float(input('Nota da primeira prova: '))
nota2 = float(input('Nota da segunda prova: '))
total = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, total))
if total < 5:
    print('O aluno foi REPROVADO!')
elif 7 > total >= 5:
    print('O aluno ficou em RECUPERAÇÃO')
else:
    print('O aluno foi APROVADO!')


 #Python Exercício 041 - Classificando Atletas


from datetime import date
nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - nascimento
print('O atleta tem {} anos em {}'.format(idade, date.today().year))
if idade <= 9:
    print('Classificação= \033[1;4;31mMirim\033[m ')
elif idade <= 14:
    print('Classificação= \033[1;4;32mInfantil\033[m')
elif idade <= 19:
    print('Classificação= \033[1;4;33mJunior\033[m')
elif idade <= 25:
    print('Classificação= \033[1;4;34mSenior\033[m')
else:
    print('Classificação= \033[1;4;35mMaster\033[m')


    # ExercícioPython 042 - Analisando Triângulos v2.0


seg1 = float(input('Primeiro segmento do triângulo: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos acima PODEM formar um triângulo ', end='')
    if seg1 == seg2 == seg3:
       print('EQUILÁTERO')
    elif seg1 != seg2 != seg3 != seg1:
       print('ESCALENO')
    else: #ou seg1 == seg2 != seg3 and seg1 == seg3 != seg2 and seg2 == seg1 != seg3 and seg2 == seg3 !=seg1 and seg3 == seg1 !=seg2 and seg3 == seg2 != seg1:
       print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo:')
# equilátero se todos os lados possuem a mesma medida
# isósceles se dois lados possuem a mesma medida.
# escaleno se todos os lados possuem medidas diferentes



 #Exercício Python 043 - Índice de Massa Corporal ( IMC )

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('Seu IMC (Índice de Massa Corporal) é igual a {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso normal!')
elif 18.5 <= imc < 25:
    print('O seu peso está no nível IDEAL!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MORBIDA!')


      #Exercício Python 044 - Gerenciador de Pagamentos

# ou print('{:=^40}'.format( 'LOJINHA DO GUANABÁRA' ))PORÉM desta forma não dá para pintar duas str de cores alternadas
print('\033[1;34m=\033[m'*24, end='')
print('\033[1;44mLOJINHA DO GUANABÁRA\033[m', end='')
print('\033[1;34m=\033[m'*24)
produto = float(input('Valor das compras: R$'))

print('''Selecione uma das opções abaixo:
 [ 1 ] à vista dinheiro/PIX
 [ 2 ] à vista no cartão 
 [ 3 ] 2x no cartão
 [ 4 ] 3x ou mais no cartão                 
''')
pagamento = int(input('Selecione sua opção:'))
if pagamento == 1:
    novo = produto - (produto * 10 / 100)
elif pagamento == 2:
    novo = produto - (produto * 5 / 100)
elif pagamento == 3:
    novo = produto
    parcela = produto / 2
    print('Sua compra de R${} será parcelada em 2x de R${} SEM JUROS'.format(produto, parcela))
elif pagamento == 4:
    novo = produto + (produto * 20 / 100)
    juros = int(input('Quantas parcelas?: '))
    parcela = novo / juros
    print('Sua compra de R${} será parcelada em {}x de R${} COM JUROS'.format(produto,juros, parcela))
else:
    novo = 0
    print('Opção inválida. Tente novamente!')
print('Sua compra no valor de R${:.2f}, no final, ficará no valor de R${:.2F}'.format(produto,novo))


 # Exercício Python 045 - GAME: Pedra Papel e Tesoura

import emoji
from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 3)
while True:
    print(''' Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
    ''')
    jogador = int(input('Qual é a sua jogada? '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!')
    print('{:=^40}'.format('Resultado'))
    print('Computador: {}'.format(itens[computador]))
    print('Jogador: {}'.format(itens[jogador]))
    print('='*40)
    if computador == 0: #computador jogou PEDRA
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('Você VENCEU!!!')
        elif jogador == 2:
            print('Você PERDEU!')
    elif computador == 1: #computador jogou PAPEL
        if jogador == 0:
            print('Você PERDEU!')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('Você VENCEU!!!')
    elif computador == 2: #computador jogou TESOURA
        if jogador == 0:
            print('Você VENCEU!!!')
        elif jogador == 1:
            print('Você PERDEU!')
        elif jogador == 2:
            print('EMPATE!')
    r = str(input('Deseja continuar?[S/N] '))
    if r in 'Nn':
        break

# SIMPLIFICANDO...
'''import random
print ("VAMOS JOGAR PEDRA, PAPEL E TESOURA!")
a = int(input("Considere:\n1 = PEDRA\n2 = PAPEL\n3 = TESOURA\nAgora, digite sua escolha: "))
b = random.randint(1,3)
print (b)
if a == b:
    print ("EMPATE")
elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print ("VOCÊ PERDEU!")
else:
    print ("VOCÊ GANHOU")'''



