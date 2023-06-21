
                           #  Curso Python #23 - Tratamento de Erros e Exceções

try: # tente ler isto
    a = int(input('numerador: '))
    b = int(input('denomindaor: '))
    r = a / b
except Exception as erro: # para formatar como classe, causa, contexto etc
   print(f'Problema encontrado foi {erro.__class__}') # classe do erro (ex:ValueError)
else: # Deu certo
    print(f'O resultado foi: {r:.1f}')
finally: # acontece independente de Certo/Errado
    print('Volte sempre')

''' ou...
except: # Deu erro
    print('Tivemos um problema:( ' '''



try: # tente ler isto
    a = int(input('numerador: '))
    b = int(input('denomindaor: '))
    r = a / b
except (ValueError, TypeError): # erro de Valor ou de Tipo
   print('Tivemos um problema com os tipos de dados que você digítou')
except ZeroDivisionError: # se dividir por 0
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt: # caso não informe os dados
    print('O usuário optou por não informar os dados!')
except Exception as erro:
    print(f'O problema encontrado foi {erro.__cause__}')
else: # Deu certo
    print(f'O resultado foi: {r:.1f}')
finally: # acontece independente de Certo/Errado
    print('Volte sempre')



                             # Exercício Python #113 - Funções aprofundadas em Python

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[;31mErro! Tente usar números Inteiros válidos!\033[m')
        if ok:
            break
    return valor


def leiafloat(a):
    ok = False
    valor = 0
    while True:
        n = str(input(a)).strip()
        if n.isnumeric():
            valor = float(n)
            ok = True
        else:
            print('\033[;31mErro! Tente usar números Reais válidos!\033[m')
        if ok:
            break
    return valor

try:
    n = leiaint('Digíte um número Inteiro: ')
    a = leiafloat('Digíte um número Real: ')
    print(f'O valor Inteiro digitado foi {n} e o Real {a}')
except KeyboardInterrupt:
    print('\033[;31mO usuário optou por não informar os dados!\033[m')



'''                           Solução Guanabára:

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digíte um número inteiro válido!')
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digíte um número Real válido!')
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n


n1 = leiaint('Digíte um número Inteiro: ')
n2 = leiafloat('Digíte um número Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
'''



                              # Exercício Python #114 - Site está acessível?

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento:( ')
else:
    print('Consegui acessar o site Pudim com sucesso! ')
    print(site.read) # mostrar o CONTEÚDO em HTML do site



                          # Exercício Python #115a - Criando um menu em Python

# DIRETÓRIO
