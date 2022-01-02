x=float(input('digite o primeiro número: '))
y=float(input('digite o segundo número: '))
z=float(input('digite o terceiro número: '))
maior=x
menor=x
#if x >= y and x >= z:
   # maior=x
if y >= x and y >= z:
    maior=y
elif z >= x and z >= y:
    maior=z
#if x <= y and x <= z:
    #menor=x
if y <= x and y <= z:
    menor=y
elif z <= x and z <= y:
    menor=z
print('O maior número é {} e o menor é {}.'.format(maior,menor))
