somaidade=0
maioridadehomem=0
nomevelho=''
totmulher20=0
for p in range(1,5):
    print('-----{}ª PESSOA-----'.format(p))
    nome=input('nome: ').strip()
    idade= int(input('idade: '))
    sexo=input('sexo[M/F]:').strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridade=idade
        nomevelho=nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade=somaidade/4
print('a media de idade do grupo é de {} anos'.format(mediaidade))
print('o homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomevelho))
print('ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
