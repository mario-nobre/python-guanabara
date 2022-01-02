from datetime import date
ano=int(input('digite um ano ou zero para  o ano atual '))
if ano==0:
    ano=date.today().year
if ano%4==0 and not ano%100==0 or ano%400==0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
