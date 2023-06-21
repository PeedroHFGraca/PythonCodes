                             # Exercício 16# Quebrando um número


from math import trunc

n = float(input("Digite um número com vírgula:"))
tru = trunc(n)
print("O valor digitado foi {}. Sua porça inteira é {}".format(n, tru))


                                  # Exercício 17# Hipotenusa


from math import hypot

co = float(input("Comprimento do Cateto Oposto:"))
ca = float(input("Comprimento do Cateto Adjacente:"))
# hi = (co ** 2 + ca ** 2) ** (1/2)
hi = hypot(co, ca)
print("A Hipotenusa vai medir {:.2f}".format(hi))


                             # Exercício 18# SENO, COSSENO, TANGENTE


import math
ângulo = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {}ª tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {}ª tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {}ª tem TANGENTE de {:.2f}'.format(ângulo, tangente))


                            # Exercício 19# Sorteando um ítem na lista


import random
nome1 = str(input('Digíte o primeiro nome:'))
nome2 = str(input('Digite o segundo nome:'))
nome3 = str(input('Digíte o terceiro nome:'))
lista = (nome1, nome2, nome3)
sorteado = random.choice(lista)
#random (escolher aleatóriamente)
print('O nome sorteado foi {}'.format(sorteado))


                           # Exercício #020 Sorteando uma ordem na lista


from random import shuffle
n1 = input('Digíte o primeiro nome:')
n2 = input('Digíte o segundo nome:')
n3 = input('Digíte o terceiro nome:')
list = [n1,n2,n3]
random.shuffle(list)
#shuffle = bagunçar ordem de apresentação
print('A ordem de apresentação será: {}'.format(list))


                                   # Exercício #21 - Musica mp3.


#baixar a musica, renomear como mp3, recortar e colar aqui
import pygame
pygame.mixer.init()
pygame.init()#iniciar
pygame.mixer.music.load('mus.mp3')
pygame.mixer.music.play()
pygame.event.wait()


