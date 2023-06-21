from ex115a.lib.interface import *
from ex115a.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    from time import sleep
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        LerArquivo(arq)
    elif resposta == 2:
        # opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('\033[1mSaindo do sistema... Até logo!\033[m',)
        break
    else:
        print('\033[31mERRO! Digíte uma opção válida!\033[m')
    sleep(2)