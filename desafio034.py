sal=float(input('Qual o valor do seu salário? '))
if sal>1500:
    i=10
    aum=sal*i/100
else:
    i=15
    aum=sal*i/100
print('o aumento do seu salário é de {}%.'.format(i),end='\u263a')
print(' E o seu aumento será de R${:.2f}.'.format(aum))
print('você vai passar a ganhar R${:.2f}.'.format(sal+aum))
