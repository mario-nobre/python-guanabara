co=float(input('digite a medida do cateto oposto '))
ca=float(input('digite a medida do cateto adjacente '))
from math import hypot
h=hypot(co,ca)
print('a hipotenusa do triângulo retângulo tem medida de {}'.format(h))
