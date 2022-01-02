from datetime import date
atual=date.today().year
nasc=int(input('ano de nascimento: '))
idade=atual-nasc
print('quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade==18:
    print('você tem que se alistar imediatamente')
elif idade<18:
    saldo=18-idade
    print('você ainda não tem 18 anos. ainda falta {} anos para o alistamento'.format(saldo))
    ano=atual+saldo
    print('seu alistamento será em {}'.format(ano))
else:
    saldo=idade-18
    print('você ja deveria ter se alistado há {} anos'.format(saldo))
    ano=atual-saldo
    print('seu alistamento foi em {}'.format(ano))
