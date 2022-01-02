r1=float(input('qual o comprimento da reta 1? '))
r2=float(input('qual o comprimento da reta 2? '))
r3=float(input('qual o comprimento da reta 3? '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('pode formar um triângulo.')
else:
    print('não pode formar um triângulo')
