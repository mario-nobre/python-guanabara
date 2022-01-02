dist=float(input('qual a distancia da viagem em km? '))
if dist<=200:
    preco=0.50*dist
else:
    preco=0.45*dist
print('a passagem será de R${:.2f}.'.format(preco))
