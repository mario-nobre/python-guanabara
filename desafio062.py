print('gerador de pa')
print('-='*15)
primeiro = int(input('primeiro termo: '))
razão=int(input('razão: '))
termos=9
cont=0
print(primeiro,end='-')
while termos != 0:
    for x in range(0,termos):
        primeiro += razão
        print(primeiro,end='-')
        cont += 1
    print('pausa')
    termos=int(input('deseja mais quantos termos?'))
print('progressão finalizada com {} termos mostrados'.format(cont+1))
