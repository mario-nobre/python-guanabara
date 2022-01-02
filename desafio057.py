sexo=input('informe o seu sexo: [M/F]').strip().upper()[0]
while sexo not in 'MF':
    sexo=input('dados inválidos. por favor , informe seu sexo: ').strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))
