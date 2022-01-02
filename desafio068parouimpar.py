from random import randint
jogador = 0
computador = 0
while True:
    print('=-'*15)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-'*15)
    jog = int(input('Diga um valor: '))
    cpu = randint(0,10)
    soma = jog + cpu
    escolha = input('Par ou Impar? [P/I]').lower().strip()[0]
    print(f'cpu jogou {cpu} e jogador jogou {jog}. a soma é {soma}.')
    if soma % 2 == 0:
        resultado = 'p'
    else:
        resultado = 'i'
    if escolha == resultado:
        print('você venceu')
        jogador += 1
        vencedor = 'jogador'
    else:
        print('você perdeu')
        computador += 1
        vencedor = 'computador'
    if jogador == 3 or computador == 3:
        print('FIM DE JOGO')
        print(f'''
        placar:
jogador {jogador} x {computador} cpu
{vencedor} venceu!''')
        break
