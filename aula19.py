
                                           #Curso Python 19 - Dicionários

dados = dict() # ou apenas {}
dados = {'nome':'Pedro', 'idade':25} # 'nome' e 'idade' são os identificadores das variáveis 'Pedro' e 25
print(dados['nome']) #  Pedro
print(dados['idade']) # 25

dados['sexo'] = 'M' # adicionar variáveis nos Dicionários - identificador 'Sexo' recebe variável 'm'
del dados['idade'] # excluir variável 25

filme = {
    'título':'Star Wars',
    'ano':1977,
    'diretor':'George Lucas'
}
print(filme.values()) # 'Star wars', '1977', 'George Lucas'
print(filme.keys()) # 'título', 'ano', 'diretor'
print(filme.items()) # pegará os dois
for k, v in filme.items():
    print(f'O {k} é {v} ')


pessoas = {'nome':'Pedro', 'sexo':'M', 'idade':18}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} e é do sexo {pessoas["sexo"]}')
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')


brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]) # {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
print(brasil[0]['UF']) # 'Rio de janeiro'
print(brasil[1]['Sigla']) # SP



estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativda: '))
    estado['Sigla'] = str(input('Silga do Estado: '))
    brasil.append(estado.copy()) # copiando o Dicionário 'estado'
print('-'*10)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()


