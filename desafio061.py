print('gerador de pa')
print('-='*15)
primeiro=int(input('primeiro termo: '))
razão=int(input('razão da P.A: '))
termo=primeiro
cont=1
while cont <= 10:
    print('{} -'.format(termo),end='')
    termo += razão
    cont += 1
print('FIM')
