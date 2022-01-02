#soma=0
#for c in range(3,501,6):
#    soma=soma+c
#print(soma)

#ou
soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma += c  # soma = soma+ c
        cont += 1  # cont = cont + 1
print('a soma de todos os {} valores é {}'.format(cont,soma))
