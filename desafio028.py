from random import randint
from time import sleep
cpu=randint(0,5)#sorteia um número nesse intervalo.
print('=-='*25)
print('VAMOS BRINCAR. TENTE ADIVINHAR O NÚMERO QUE ESTOU PENSANDO DE 0 A 5.')
print('=-='*25)
num=int(input('Digite o número que estou pensando: '))
print('aguarde um momento...')
sleep(2)
if num==cpu:
    print('correto! você venceu!')
else:
    print('errado! o número era {}.'.format(cpu))
