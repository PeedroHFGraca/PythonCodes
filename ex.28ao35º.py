
                             # Exercício Python 028 - Jogo da Adivinhação v.1.0


from random import randint
from time import sleep
import emoji

computador = randint(0, 5)  # dizer aleatóriamente um número de 0 a 5
print('\033[1;34m-=-\033[m' * 20)

print('                  \033[1;4;44mJogo da adivinhção\033[m', end='  ')
print(emoji.emojize(':thinking_face:'))
print('\033[1;7mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')

print('\033[1;34m-=-\033[m' * 20)
jogador = int(input('Qual foi o número?:'))
print('PROCESSANDO...')
sleep(1.5)
if jogador == computador:
    print('PARABÉNS! Você me venceu ', end='')
    print(emoji.emojize(':worried_face:'))
else:
    print('GANHEI! O número em que pensei foi {} e não {}. Mais sorte na próxima vez!'.format(computador, jogador), end='  ')
    print(emoji.emojize(':smiling_face_with_sunglasses:'))



                                # Exercício Python 029 - Radar eletrônico

velocidade = float(input('Qual é a velocidade atual do carro? Km'))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h.')
    multa = (velocidade - 80) * 7
    # a multa vai custar R$7 a cada Km acima do limite
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha  um bom dia! Dirija com cuidado!')



                                # Exercício Python 030 - Par ou Ímpar?


número = int(input('Digíte um número qualquer:'))
resultado = número % 2
# no resto da divisão (%) de todo número PAR por 2 vai dar 0 e de todo numero ÍMPAR será igual a 1
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é ÍMPAR'.format(número))




                                 # Exercício Python 031 - Custo da Viagem

    distancia = float(input('Qual é a distância da sua viagem? Km'))
    print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
    valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45
    print('O preço de sua passagem é de R${:.2f}'.format(valor))

'''  Ou podemos utilizar... 

if distancia <= 200:
  valor = distancia * 0.5
  print('O preço de sua passagem é de R${}'.format(valor))
else:
  valor = distancia * 0.45
  print('O preço da sua viagem é de R${:.2f}'.format(valor))

'''



                                    # Exercício Python 032 - Ano Bissexto


from datetime import date

ano = int(input('\033[1;4;7mAno Bissexto?\033[m \nQual ano deseja analisar? Digite 0 para selecionar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # != diferente, não igual a...
    print('O ano {} É BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO.'.format(ano))



                                  # Exercício Python 033 - Maior e menor valores

a = int(input('primeiro valor:'))
b = int(input('segundo valor:'))
c = int(input('terceiro valor:'))
# verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))



                                # Exercício Python 034 - Aumentos múltiplos


salario = float(input('Qual é o salario do funcionário?'))
print('O salário é de R${:.2f}'.format(salario))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    a = '15%'
else:
    novo = salario + (salario * 10 / 100)
    a = '10%'
print('Com um aumento de {} o salário do funcionario passou de {:.2f} para {:.2f}'.format(a, salario, novo))



                             # Exercício Python 035 - Analisando Triângulo v1.0

r1 = float(input('Primeiro seguimento'))
r2 = float(input('Segundo seguimento'))
r3 = float(input('Terceiro seguimento'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O seguimento acima PODEM FORMAR um triângulo')
else:
    print('O seguimento acima NÃO PODE FORMAR um triângulo')