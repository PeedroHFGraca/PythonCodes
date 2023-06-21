
                                                  # Aula 10

nome = str(input('Qual é o seu nome?: '))
if nome.upper() == 'KETHELLYN':
     print('Olá, Dra Kethellyn Feitosa!')
else:
     print('Olá,{}!'.format(nome))

n1 = float(input('Nota da primeira prova:'))
n2 = float(input('Nota da segunda prova:'))
m = (n1+n2) / 2
print('A sua média foi {:.1f}.'.format(m))
if m < 6.0:
    print('Média ruim. ESTUDE MAIS!')
else:
    print('Média boa. PARABÉNS!')

