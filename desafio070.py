total=totmil=menor=cont=0
barato=''
while True:
    produto=input('nome do produto: ')
    preço=float(input('preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp=input('quer continuar? [S/N]').strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'o total de compra foi R${total:.2f}')
print(f'temos {totmil} produtos custando mais de 1000.00')
print(f'o produto mais barato foi {barato} que custa R${menor:.2f}')
