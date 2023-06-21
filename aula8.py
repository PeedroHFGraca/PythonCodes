# Bibliotecas - Math:

# ceil / flooR (arredondar para cima/baixo)
# trunc (desconsidera a parte com vírgula do número)
# pow (potência)
# sqrt SquareRoot (raiz quadrada)
# factorial (fatorar)
# Emojis aqui!

import math

num = int(input('Digite um número:'))
raÍz = math.sqrt(num)
print('A raÍz de {} é igual a {}.5'.format(num, math.ceil(raÍz)))
'''irá arredondar o resultado (CEIL).'''

# from MATH import Ceil = da Biblioteca Math importar somente Ceil

from math import sqrt

n1 = int(input('Digite um numero:'))
raz = sqrt(n1)
print('A raíz de {} é igual a {}.'.format(n1, raz))

import emoji

print(emoji.emojize("Python é :thumbsup: :lips:", language='alias'))
print(emoji.emojize(":red_heart:"))
print(emoji.demojize('😃')) # para ver o cógido do EMOJI



