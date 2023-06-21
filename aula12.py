
 #Curso Python 012 - Condições Aninhadas


nome = str(input('Digite seu nome:'))
if nome.upper() == 'PEDRO':
    print('Que nome bonito!!!')
elif nome == 'Paulo' or nome == 'Lucas' or nome == 'Gustavo':
    print("Seu nome é bem popular no Brasil.")
elif nome in 'Kethellyn Elisabeth Neide':
    print('Que belo nome feminino!!!')
else:
    print('Seu nome é bem normal.')
print('Tenha um ótimo dia, {}!'.format(nome))