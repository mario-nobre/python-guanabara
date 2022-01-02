from random import randint
computador = randint(0,10)#sorteia um número nesse intervalo.
print('=-='*25)
print('VAMOS BRINCAR. TENTE ADIVINHAR O NÚMERO QUE ESTOU PENSANDO DE 0 A 10.')
print('=-='*25)
acertou=False
palpites=0
while not acertou:
    jogador=int(input('Digite o número que estou pensando: '))
    palpites += 1
    if jogador == computador:
        acertou=True
    elif jogador < computador:
        print('é mais....tente novamente.')
    else:
        print('é menos...tente novamente.')
print('acertou com {} tentativas.'.format(palpites))
