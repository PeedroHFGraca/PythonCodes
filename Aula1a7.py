# Comentário
# tipos primitivos: int= inteiro, float= números reais, boot= True or False, str= string

nome = input('Digite seu nome:')
print('É um prazer te conhecer,', nome)

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1 + n2
# : print('A soma entre', n1, 'e', n2, 'é igual a:', s)
print('A soma entre {} e {} é igual a: {}'.format(n1, n2, s))

n = input("Digite algo:")
print('O tipo primitivo deste valor é:', type(n))
print('É numérico?', n.isnumeric())
print('É alfabético?', n.isalpha())  # alpha = é letra?
print('É alfanumérico?', n.isalpha())
print('Está em maiúsculas?', n.isupper()) #palavra inteira em maiúscula
print('Está em minúsculas?', n.islower()) #palavra inteira em minúscula

number = int(input('Digite um número:'))
d = number * 2
t = number * 3
r2 = number ** (1/2)
print('O dobro do número que você digitou é igual a: {}. \nO triplo: {}. \nE a raiz quadrada: {:.2f}'.format(d, t, r2))
a = number - 1
s = number + 1
print('Analisando o valor {}, seu antecessor é {} e o seu sucessor {}'.format(number, a, s))
