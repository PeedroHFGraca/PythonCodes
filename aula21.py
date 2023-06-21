
                                # Curso Python 21 - Funções (Parte 2)
'''
-help()                  parâmetros opcionais                 variável local
-docstrings              Escopo de variáveis                  return - Retornando valores
'''
# help() Ajuda interna = ir em Python Console (inferior da tela) e digitar a function help()
# ou help(função), ex: help(print)
# ou print(input.__doc__) - informações sobre Input
# Docstring = manual que vai ser exibido durante a ajuda interativa (Você mesmo cria):
# Para cada Função criada (Def.), podemos usar um Docstring como manual que será exibido durante a ajuda interativa


def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela:
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return:  Sem retorno
    Criado por Pedro Henrique Ferreira Graça
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

# contador(0, 10, 2)
help(contador) # mostrar o manual da função criada por mim 'contador'




# Parâmetros opcionais == podemos ou não declarar os parâmetros
# def somar(a, b, c=0): # apenas o parâmetro C é opcional, o restante é obrigatório
# def somar(a, b=0, c=0): # B e C opcionais
def somar(a=0, b=0, c=0): # todos parâmetros opcionais
    s = a + b + c
    print(f'A soma dos valores vale {s}')

somar() # A soma dos valores vale 0, pois não foi definido nenhum valor
# somar (c=4, a=1) - Posso nomear meus parâmetros. Neste exemplo, o B não tem valor






                   # Escopo de variáveis: Local onde a variável vai e não vai existir

def teste():
    x = 8 # variável local, como está ligada ao Def, será lida apenas no seu seguimento e não fora dele
    print(f'Na função teste, n vale {n}') # variável global
    print(f'Na função teste, x vale {x}') # variável local

# Programa Principal
n = 2
print(f'No programa principal, N vale {n}') # N variável global
teste()
print(f'No programa principal, X vale {x}')# programa dará erro, pois X é uma variável local, pertence ao Def e por isso
# não pode ser lido fora dele



def function():
    n1 = 4 # local
    print(f'N1 dentro vale {n1}')


n1 = 2 # global
function()
print(f'N1 do lado de fora vale {n1}')
# Neste caso, temos uma variável N1 subdivida em 2: variável global e variável local




                                                # IMPORTANTE!!!
def teste(b):
    global a # a variável 'A' permanecerá como global...
    a = 8 # a variável 'A' deixará de valer 5 para valer 8
    b += 4 # Neste momento B vale o primeiro valor de 'a' = 5, pois é o parâmetro de 'a'
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


# Programa principal
a = 5 # variável global
teste(a)
print(f'A fora vale {a}')



                                       #Return - Personalização dos resultados

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cáuculos deram {r1}, {r2} e {r3}.')



def fatorial(num=1): #caso não receba nenhum valor, o parâmetro será 1
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


# O fatorial de um número é a multiplicação desse por todos os seus antecessores maiores que zero
n = int(input('Digíte um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

''' ou

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(1)
print(f'Os resultados são {f1}, {f2} e {f3}')

'''


# Return valor lógico True or False
def par(n=0): # se não passar nenhum número ele é 0
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digíte um número: '))
if par(num):
    print('É Par! ')
else:
    print('Não é par!')



