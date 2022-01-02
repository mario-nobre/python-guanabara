from random import randint
from time import sleep
itens=('pedra','papel','tesoura')
computador=randint(0,2)
print('''Suas opões:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador=int(input('qual é a sua jogada? '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('jogada invalida! tente novamente.')
    quit()
print('JÓ')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-='*11)
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {} '.format(itens[jogador]))
print('-='*11)
if computador == 0: #jogada do computador
    if jogador ==0:
        print('EMPATE')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('computador vence')
    else:
        print('jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('computador vence')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador vence')
    else:
        print('jogada inválida!')
elif computador == 2:
    if jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('computador vence')
    elif jogador == 2:
        print('empate')
    else:
        print('jogada inválida!')
