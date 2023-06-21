# Curso Python  20 - Funções (Parte 1)

'''
Função exemplos: .upper() ; print() ; len() ; int()
'''


def linha():  # Def = definição de ... (variável linha)  //  'def' CRIA funções personalizadas
    print('-' * 30)


linha()
print('CURSO EM VÍDEO')
linha()
print('PROGRAMA EM PYTHON')
linha()
print('SEJA UM PROGRAMADOR')


# Simplificando o código acima...
def título(txt):
    print('- ' * 30)
    print(txt)
    print('- ' * 30)


título('CURSO EM VÍDEO')
título('PROGRAMA EM PYTHON')
título('SEJA UM PROGRAMADOR')

a = 4
b = 5
s = a + b
print(s)

a = 1
b = 2
s = a + b
print(s)

a = 6
b = 1
s = a + b
print(s)


# Simplificando cód acima
def soma(a, b): # caso não seja informado 2 parâmetros o programa dará erro
    s = a + b
    print(s)


soma(4, 5)
soma(1, 2)
soma(6, 1)


# definindo parâmetros
def soma(a, b):
    print(f'A = {a}, B = {b}')
    s = a + b
    print(f'A soma A+B = {s}')


soma(b=4, a=5) # B pode ser 4 ou 5


# DESEMPACOTAMENTO - Multiplos parâmetros
def contador(* num): # criará uma tupla com os vários parâmetros, independente da quantidade
    tamanho = len(num)
    print(f'Recebi os valores {num}. Ao todo são {tamanho} números')


contador(1, 5, 6, 7)
contador(10, 20)


#
def dobrar(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [1, 2, 3, 4]
print(valores)
print('Dobrando valores...  ')
dobrar(valores) # CRIEI uma função para dobrar os valores da 'Lista' valores
print(valores) # mostrará o dobro de cada valor dentro de 'Valores'


def soma(* valores):# Multiplos parâmetros
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores}, temos {s}')


soma(5, 10)
soma(2, 4)


