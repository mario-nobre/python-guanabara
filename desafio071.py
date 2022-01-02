print('='*30)
print('{:-^30}'.format('banco cev'))
print('='*30)
valor=int(input('que valor você quer sacar? R$ '))
tot50=valor//50
valor=valor-tot50*50
tot20=valor//20
valor=valor-tot20*20
tot10=valor//10
valor=valor-tot10*10
tot1=valor
if tot50 > 0:
    print('total de {} cédulas de R$50'.format(tot50))
if tot20 > 0:
    print('total de {} cédulas de R$20'.format(tot20))
if tot10 > 0:
    print('total de {} cédulas de R$10'.format(tot10))
if tot1 > 0:
    print('total de {} cédulas de R$1'.format(tot1))
print('='*30)
print('volte sempre!')
