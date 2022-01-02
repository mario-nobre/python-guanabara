km=float(input('quantos km você rodou? '))
d=int(input('quantos dias alugados?'))
p=60*d+0.15*km
print('o total a pagar é de R${:.2f}'.format(p))
