a=float(input('digite o valor do ângulo '))
import math
rad=math.radians(a)
sen=math.sin(rad)
cos=math.cos(rad)
tang=math.tan(rad)
print('para o ângulo de {}°, temos que:\nseno={:.2f} \ncosseno={:.2f} \ntangente={:.2f}'.format(a,sen,cos,tang))
