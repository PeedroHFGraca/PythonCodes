
# Curso Python - Mundo 3 #Aula 16 - Variáveis compostas - Tuplas


# lache = () [] {}
# () TUPLAS, [] LISTA, {} DICIOÁNRIO
lanche = ('Hambúrguer', 'Suco', 'Batata frita', 'Sorvete')  # índice (0,4), desconsidera o último número
print(lanche)
print(lanche[0])
print(lanche[3])
print(lanche[1:4])
print(lanche[:2])
print(lanche[2:])
print(lanche[-1])  # mostrará SORVETE. último item da variável é = -1
print(lanche[-3])

# TUPLAS SÃO IMUTÁVEIS = NÃO CONSIGO ALTERAR SEU VALOR
# CÓDIGO ABAIXO NÃO FUNCIONARÁ
# lanche[1] = 'alguma coisa'
# print(lanche[1])

lanche = 'Hambúrguer', 'Suco', 'Batata frita', 'Sorvete'
print('O combo do meu lanche vem', len(lanche), 'itens') # LEN contar


lanche = 'Hambúrguer', 'Suco', 'Batata frita', 'Sorvete'

for comida in lanche: # dessa forma não dá para dizer a posição das str
    print(f'Eu comi {comida}')

for cont in range(0, len(lanche)): # posição da str
    print(f'Vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche): # posição da str
    print(f'Eu vou comer {comida} na posição {pos} ')

print('Comi pra caramba!')

lanche = 'Hambúrguer', 'Suco', 'Batata frita', 'Sorvete'
print(sorted(lanche)) # sorted - Organizar (no caso organizará pela quantidade de letras.


a = 1, 1, 2, 3
b = 4, 5, 6
c = a + b
print(c) # 1, 2, 3, 4, 5, 6
print(len(c)) # mostrará quantos caractéres
print(c.count(1)) # contar quantas vezes o caractere em () aparece
print(c.index(5)) # mostrar em qual posição está o número em ()
print(c.index(1, 1)  )# ^... a partir do caractére 1

pessoa = 'Pedro', 18, 'Masculino', 67, 'Kg' # podemos usar letras e números
del(pessoa) # deletará TUPLA





