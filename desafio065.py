resp='S'
soma=quant=maior=menor=0
while resp in 'Ss':
    num=int(input('digite um  numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = input('quer continuar? [S/N] ').upper().strip()[0]
media=soma/quant
print('você digitou {} numeros e a media foi {}'.format(quant,media))
print('o maior valor foi {} e o menor foi {}'.format(maior,menor))
