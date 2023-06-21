teste = list()
teste.append('Pedro')
teste.append(18)
galera = []
galera.append(teste[:]) # Cópia da lista teste
teste[0] = 'Paulo'
teste[1] = 19
galera.append(teste[:])
print(galera)

galera = [['Pedro', 19], ['Paulo', 53], ['Lucas', 24]]
#               0     1        0      1       0      1
#
#           ^ Índice 0     ^ Índice 1     ^ Índice 2

print(galera[0][0]) # do Índice [0] mostrar 'Pedro'[0]
print(galera[1][1]) # do Índice [1]mostrar  '53'[1]
print(galera[2][0]) # do Índice [2] mostrar 'Lucas'[0]
print(galera[1]) # do Índice [1] mostrar tudo ( 'Paulo', 53 )

galera = [['Pedro', 18], ['Paulo', 53], ['Lucas', 24]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

galera = list()
dado = []
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print('-='*30)
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print('-='*30)
print(f'Temos {totmaior} maiores e {totmenor} menores de idade')

