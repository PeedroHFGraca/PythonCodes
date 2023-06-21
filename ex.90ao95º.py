
                                 # Exercício Python #090 - Dicionário em Python

# minha solução
n = {}  # dict()
list = []
n['nome'] = str(input('Nome: '))
list.append(n)
n['média'] = float(input(f'Média de {n["nome"]}: '))
list.append(n)
print(f'A média de {n["nome"]} é = {n["média"]}')
if n["média"] <= 5:
    print('Situação: Reprovado!')
else:
    print('Situação: Aprovado!')

# Solução Guanabara
aluno = {}  # dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno["média"] >= 7:
    aluno['Situação'] = 'Aprovado!'
elif 5 <= aluno['média'] < 7:
    aluno['Situação'] = 'Recuperação!'
else:
    aluno['Situação'] = 'Reprovado!'
print('-=' * 30)
for k, v in aluno.items():
    print(f'  -{k} é igual a {v}')




                                     #Exercício Python  091 - Jogo de Dados em Python

from random import randint
from time import sleep
from operator import itemgetter
jogo = { 'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)# key=itemgetter(0) key,  (1)-  value
print('-='*15)
print(' == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}') # v[0] JOGADOR / v[1] Randint
    sleep(1)





                              # Exercício Python 092 - Cadastro de Trabalhador em Python

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.today().year - nasc
dados['Ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['Ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = int(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
    #35 é o tempo de contribuição
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor:  {v}')





                               # Exercício Python 093 - Cadastro de Jogador de Futebol


jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'  Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'  O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'  O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i} fez {v} goals')
print(f'Totalizando {jogador["total"]} gols')






                              # Exercício Python  094 - Unindo dicionários e listas

list = []
dados = dict()
med = soma = 0
while True:
    dados['Nome'] = str(input('Nome: '))
    while True:
        dados['Sexo'] = str(input('Sexo:[M/F] ')).strip().upper()
        if dados['Sexo'] in 'MF':
            break
        print('Erro! Por favor, responda apenas com M ou F.')
    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']
    list.append(dados.copy())
    while True:
        r = str(input('Deseja continuar?[S/N] ')).strip().upper()
        if r in 'SN':
            break
        print('Por favor, responda apenas com S ou N')
    if r == 'N':
        break
print('-=' * 30)
print(list)
print('-=' * 30)
print(f'No total há {len(list)} pessoas cadastradas')
med = soma / len(list)
print(f'A média de idade é {med:5.2f} anos')
print('As mulheres cadastradas foram: ', end='')
for p in list:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}, ')
print('A lista de pessoas acima da média : ')
for p in list:
    if p['Idade'] >= med:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')

'''a - qnt pessoas cadastradas
b - média de idade
c - qnt mulheres cadastradas
d - lista pessoas acima da méd'''





                                  # Exercício Python 095 - Aprimorando os Dicionários

jogador = {}
partidas = []
time = []

while True:
    jogador.clear() # limpar dados anteriores para pode registrar os próximos
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'  Quantos gols na partida {c+1}? '))) # qntd de gols armazenados na Lista 'PARTIDA'
    jogador['gols'] = partidas[:] # No dicionário Jogador, o campo 'gols', recebe a cópia da lista Partidas(qnt de gols)
    jogador['total'] = sum(partidas) # No dicionário Jogador, o campo 'total' recebe e soma 'partidas' (qnt de gols)
    time.append(jogador.copy()) # a lista 'time' faz uma cópia do dicionário 'jogador' = (jogador.copy )

    while True:
        r = str(input('Deseja continuar?[S/N] ')).upper().strip()
        if r in 'SN':
            break
        print('ERRO! Responda corretamente!')
    if r == 'N':
        break
# mostrar resultado:
print('-=' * 30)
print('Cód ', end='')
for i in jogador.keys():      # mostrará os campos NOME, GOLS e TOTAL
    print(f'{i:<15} ', end='')
print()
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não há jogador com o código {busca}')
    else:
        print(f' --- LEVANTAMENTO DE DADOS DO JOGADOR: {time[busca]["nome"]} --- ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   Na {i+1}ª partida {jogador["nome"].upper()} fez {g} gols.')
    print('-='* 30)
print('<< VOLTE SEMPRE >>')
