
# Curso Python - Aula 013 - Estrutura de repetição FOR

for contar in range(0, 6):  # contará como 5, pois NUNCA conta o ultimo numero
    print('Vai escrever 5 vezes a mesma coisa')

for contar in range(0, 6):
    print(contar)  # vai contar de 0 a 5

for contar in range(1, 6):
    print(contar)  # vai contar de 1 a 5

for contar in range(7, 0, -1):
    print(contar)# vai contar em ordem decrescente!

for contar in range(7, 0, 2):
    print(contar)  # contar de dois em dois

for contar in range(0, 3):
    n = int(input('Digíte um valor: '))
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passos: '))
for contar in range(i, f+ 1, p):
    print(contar)

s = 0  # S será a soma ( S = 0 )
for contar in range(0, 3):  # perguntará 3 vezes
    n = int(input('Digíte um valor: '))
    s += n  # ou S = S+N /
print('A somatória dos valores acima é igual a: {}'.format(s))



