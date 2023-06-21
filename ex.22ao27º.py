
                                # Exercício 22 - Aula #09 - Analisador de Texto


nome = str(input('Digíte seu nome completo completo:')).strip()
# strip não conta os espaços antes e depois da palavra, somente os espaços entre as palavras, só pode ser usado em STRINGS (CADEIA DE CARACTÉRES)
print('Analisando seu nome...')
print("Seu nome completo em maiúsculas: {}.".format(nome.upper()))
print('Seu nome completo em minúsculas: {}'.format(nome.lower()))
print('Seu nome completo possuí {} caractéres.'.format(len(nome) - nome.count(' '))) #contar as letras sem os espaços
# print('Seu primeiro nome tem {}.'.format(nome.find(' ')))
separa = nome.split() #criar uma lista com a resposta do usuário
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))



                            # Exercício 23 - Aula #09 - Separando dígitos de um número


num = int(input('Digíte um número:'))
# // divisão % resto da divisão
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número: {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))


                     # Exercício 24 - Aula #09 - Verificando as primeiras letras de um texto


cidade = str(input('Em que cidade você nasceu?')).strip() # tira os espaços antes e depois as palavras
print(cidade[:5].upper() == 'SANTO')


                        # Exercício Python #025 - Procurando uma string dentro de outra


nome = str(input("Digíte seu nome:")).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper())) # IN = operador python


                      #Exercício Python #026 - Primeira e última ocorrência de uma string


frase = str(input('Digíte uma frase:')).upper().strip() #não contará os espaços antes e depois da frase, mas considerará os espaços entre as palavras
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1)) # rfind = contar a partir da direita (Right)



                        #Exercício Python #027 - Primeiro e último nome de uma pessoa


n = str(input('Digíte seu nome:')).strip()
nome = n.split() #CRIAR UMA LISTA
print('Seu primeiro nome é {}'.format(nome[0])) # 0 é a primeira posição
print('Seu último nome é {}'.format(nome[len(nome)-1]))