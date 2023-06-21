
                             #Curso Python #014 - Estrutura de repetição WHILE

'''for c in range(1, 10):
    print(c)
print('FIM')
'''

c = 1
while c < 10:
    print(c)
    c += 1
print('fim')
# possuí a mesma função do FOR

n = 1
while n != 0:
    n = int(input('Digíte um valor:'))
print('FIM')
# O programa só parará quando for digítado o número 0, não possível com o For

r = 'S'
while r == 'S':
   n = int(input('Digíte um valor:'))
   r = str(input('Deseja continuar?[S/N]  ')).upper()
print('FIM')
# com o While não precisamos definir início e fim

n = 0
par = impar = 0
while n != 0:
    n = int(input('Digíte um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1


