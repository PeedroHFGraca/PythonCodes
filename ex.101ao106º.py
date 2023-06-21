
                                 # Exercício Python #101 - Funções para votação 1

# ESCOPO DE IMPORTAÇÃO — Economizando memória
# A minha solução
print('-' * 30)


def voto(nasc):
    from datetime import date # Escopo de importação, biblioteca funcionará somente em Def
    idade = date.today().year - nascimento
    print(f'Com {idade} anos: ', end='')
    if idade <= 15:
        print('Não vota.')
    elif idade >= 16 and idade < 18 or idade >= 65:
        print('Voto opicional.')
    else:
        print('Voto obrigatório!')


nascimento = (int(input('Data de nascimento: ')))
voto(nascimento)


# Solução GUANABARA:


def voto(nasc):
    from datetime import date # Escopo de importação, biblioteca funcionará somente em Def
    atual = date.today().year
    idade = atual - nasc
    if idade <= 16:
        return(f'Com {idade} anos: NÃO VOTA.')
    elif 16 <= idade >= 18 or idade >= 65:
        return(f'Com {idade} anos: Voto opicional.')
    else:
        return(f'Com {idade} anos: Voto obrigatório!')

nasc = int(input('Ano de nascimento: '))
print(voto(nasc))




                                     #Exercício Python 102 - Função para Fatorial


def fatorial(n=0, show=False):
    """
    -> Cálcula o Fatorial de um número.
    :param n: O número a ser cálculado.
    :param show: (Opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show: # Se 'show' for verdadeiro...
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#fat = int(input('Digíte um número para ver seu fatorial: '))
#print(fatorial(fat, show=True)) # Show=True = mostar o cálculo
help(fatorial)




                                    #Exercício Python  103 - Ficha do Jogador


print('-' * 25)


def ficha(jog='<desconhecido>', gol=0):# se não for informado o nome do jogador, lerá como <desconhecido>
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))  # Leremos como 'Str' pois usando 'Int' não deixa ficar em branco
if g.isnumeric(): #verificar se a str digitada é um número
    g = int(g)
else:
    g = 0
if n.strip() == '': # se tirou os espaços antes e depois da palavra e continuou vazio...
    ficha(gol=g) # ler somente os gols
else:
    ficha(n, g)




                       #Exercício Python 104 - Validando entrada de dados em Python


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input((msg))) # variável local
        if n.isnumeric(): # se 'n' for numérico...
            valor = int(n) # n fica inteiro
            ok = True
        else:
            print('\033[0;31mERRO! Escreva um número por extenso!\033[m ') # TENTE ESCREVER POR EXTENSO
        if ok:# se Ok for True
            break
    return valor


n = leiaInt('Digíte um número: ') # variável global
print(f'Você digitou o número {n}')




                              # Exercício Python 105 - Analisando e gerando Dicionários


def notas(*n, sit=False): # '*n' receber vários parâmetros, sit = situação
    """
    => DocString: Função para analisar notas e situações de vários alunos,
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação ao programa
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['Total de notas'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n) # somar 'N' e dividir(/) pela qntd de 'N' (LEN(n))
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

#Programa principal
resp = notas(5.5, 9.5, 10, sit=True) # sit=True para mostrar a situação
print(resp)
#help(notas)




                   # Exercício Python 106 - Sistema interativo de ajuda em Python


c = ('\033[m',        # 0 — sem cores
     '\033[30;41m',  # 1 — vermelho
     '\033[0;30;42m',  # 2 — verde
     '\033[0;30;43m',  # 3 — amarelo
     '\033[0;30;44m',  # 4 — azul
     '\033[0;30;45m',  # 5 — roxo
     '\033[7;1m',     # 6 — branco
    );


def ajuda(com): # função help
    título(f'ACESSANDO O MANUAL DO \'{com}\'', 4)
    print(c[6], end='') # cor fixa
    help(com)
    print(c[0], end='')

def título(msg, cor=0): #função estética / Se não colocar nada, a cor é 0 (neutra)
    tam = len(msg) + 4
    print(c[cor], end='') # iniciar as cores
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='') # encerrar as cores


#Programa principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 1)