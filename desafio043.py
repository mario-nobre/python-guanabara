peso=float(input('qual é seu peso? (kg) '))
altura=float(input('qual é sua altura? (m) '))
imc=peso/altura**2
print('o IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc <30:
    print('você está em SOBREPESO')
elif 30 <= imc < 40:
    print('você está em OBESIDADE!')
else:
    print('você está em OBESIDADE MÓRBIDA, cuidado!')
