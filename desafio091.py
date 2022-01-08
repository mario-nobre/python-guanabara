from random import randint
from time import sleep
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('=-' * 30)
flag = 1
print(' == RANKING DOS JOGADORES ==')
rank = sorted(jogadores, key=jogadores.get, reverse=True)
for i in rank:
    print(f'    {flag}° lugar: {i} com {jogadores[i]}.')
    flag += 1
    sleep(1)

'''for i, v in enumerate(rank):
    print(f'    {i+1}° lugar: {v} com {jogadores[v]}.')
    sleep(1)
    (solução guanabara)
    '''
