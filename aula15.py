
                                # Curso Python #15 - Interrompendo repetições while

n = s = 0
while True: # criando um looping eterno
    n = int(input('Digíte um número: '))
    if n == -0:
        break #quebrando o looping , impede que leia o número somado tenha o valor que impomos, no caso -0
    s += n
print(f'A soma entre os valores digítados é = {s}') #Alternativa para .format = f'numero {n} '
#print('A soma entre os valores digítados é = {}').format(s)
nome = 'Pedro!'
idade = 18
print(f'Meu nome é {nome:^20} e tenho {idade:=^6}')# :^20[qualquer numero] para centralizar a str







