print('gerador de pa')
print('-='*15)
primeiro=int(input('primeiro termo: '))
razão=int(input('razão da P.A: '))
termo=primeiro
cont=1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -'.format(termo),end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais=int(input('quantos você quer mostrar a mais? '))
print('progressão finalizada com {} termos mostrados'.format(total))
