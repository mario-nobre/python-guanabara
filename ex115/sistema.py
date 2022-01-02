from ex115.lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(1)
