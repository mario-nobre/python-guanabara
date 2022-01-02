cont=soma=0
num=int(input('digite um  umero[999 para parar]: '))
while num!=999:
    soma+=num
    cont+=1
    num = int(input('digite um  umero[999 para parar]: '))
print('você digitou {} numeros e a soma entre eles foi {}.'.format(cont,soma))
