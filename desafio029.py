vel=float(input('qual a velocidade do veiculo? '))
ddv=vel-80
multa=ddv*7
if vel<=80:
    print()
else:
    print('sua velocidade estava a {}km acima do limite permitido.\nVocê foi multado em {:.2f} reais.'.format(ddv,multa))
