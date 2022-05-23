from lib.data import *
from lib.interface import *
from time import sleep


arq = 'data.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Criar Cadastro', 'Listar Cadastros', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 2:
        lerData(arq)

    elif resposta == 3:
        print('Saindo do Sistema')
        break
    else:
        print('\033[31mERRO, digite um opção valida!\033[m')

    sleep(2)
