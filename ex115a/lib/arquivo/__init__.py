from ex115a.lib.interface import *
# * importar tudo


def arquivoExiste(nome): # Verifica se o arquivo existe
    try:
        a = open(nome, 'rt') # open abrir arquivo em rt = read and text
        a.close()
    except FileNotFoundError: # se arquivo não encontrado
        return False
    else:
        return True

def criarArquivo(nome): # Cria o arquivo cursoemvideo.txt
    try:
        a = open(nome, 'wt+') # write text, + (caso o arquivo não exista, crie)
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Ariquivo {nome} criado com sucesso')


def LerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a: # Para cada linha dentro de arquivo
            dado = linha.split(';') # dividir dados
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos') # lista - dado[0] = NOME / dado[1] = IDADE
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') # apend text = colocar mais coisas dentro do arquivo
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()