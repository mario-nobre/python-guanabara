homens = mulheres = maiores = 0
while True:
    sexo = ' '
    idade=int(input('idade: '))
    while sexo not in 'mf':
        sexo = input('sexo: [M/F]').strip().lower()[0]
    if sexo == 'm':
        homens += 1
    elif idade < 20:
        mulheres += 1
    if idade > 18:
        maiores += 1
    op = ' '
    while op not in 'sn':
        op = input('quer continuar? [S/N] ').strip().lower()[0]
    if op in 'Nn':
        print('volte sempre!')
        break
print(f'total de pessoas com mais de 18 anos: {maiores}')
print(f'ao todo temos {homens} homens cadastrados ')
print(f'e temos {mulheres} mulheres com menos de 20 anos ')
