                                    # Média do Aluno - Excercício 7

n1 = float(input('Qual foi sua nota na primeira prova?'))
n2 = float(input('Qual foi a sua nota na segunda prova?'))
m = (n1 + n2) / 2
print('Sua média é: {}'. format(m))


                             # Transformando Metros em Cm e Mm - Excercício 8

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:}cm e {:}mm'.format(medida, cm, mm))


                                        # Tabuáda - Excercício 09

num = int(input('Digite um numero para ver sua tabuada:'))
print('{} * {:2} = {}'.format(num, 1, num*1))
print('{} * {:2} = {}'.format(num, 2, num*2))
print('{} * {:2} = {}'.format(num, 3, num*3))
print('{} * {:2} = {}'.format(num, 4, num*4))
print('{} * {:2} = {}'.format(num, 5, num*5))
print('{} * {:2} = {}'.format(num, 6, num*6))
print('{} * {:2} = {}'.format(num, 7, num*7))
print('{} * {:2} = {}'.format(num, 8, num*8))
print('{} * {:2} = {}'.format(num, 9, num*9))
print('{} * {:2} = {}'.format(num, 10,num*10))


                                        #Carteira - Excercício 10

real = float(input('Quantos R$ você possuí em sua carteira? R$'))
dolar = real / 5.20
print('Com R${} é possível comprar US${}'.format(real, dolar))


                                     #Pintando parede - Exercício 11

larg = float(input('largura da parede:'))
alt = float(input('altura da parede:'))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e uma área de {}m²'.format(larg, alt, área))
tinta = área / 2
print('Para pintar sua parede você precisará de {}l de tinta'.format(tinta))


                                  #Calculando Descontos - Excercício 12

preço = float(input('Qual é o valor do seu produto? R$'))
novo = preço - (preço*5/100)
print('O produto que custava R${:.2f}, com o desconto de 5% passou a custar {:.2f}'.format(preço, novo))


                                    #Reajuste Salarial - Exercício 13

salário = float(input('Qual é o salário do funcionário? R$'))
novo = salário + (salário*15/100)
print('Um funcionario que ganhava R${:.2f}, com o aumento de 15%, passa a receber o valor de R${:.2f}'.format(salário, novo))

prod = float(input('Digite o valor do produto desejado: R$'))
avista = prod - (prod*10/100)
aprazo = prod + (prod*12/100)
print('O produto desejado custa R${}. À vista o valor será R${}, e a prazo R${}'.format(prod, avista, aprazo))


                                #Conversor de Temperaturas - Exercício 14

c = float(input('Qual é a temperatura atual? ªC' ))
f = 9 * c / 5 + 32
print('A temperatura de ªC{} é igual a {}ªF'.format(c, f))


                                     #Alugel de Carros - Exercício 15

dias = int(input('Por quantos dias o carro foi alugado?'))
km = float(input('Quantos quilometros rodados? KM'))
pago = dias * 60 + km * 0.15
print('O valor total a pagar é R${:.2f}'.format(pago))
