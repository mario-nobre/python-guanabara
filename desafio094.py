cadastro = {}
user = []
cadastro['nome'] = input('Nome: ')
while True:
    sexo = input('Sexo: [M/F]')
    if sexo in 'mM' or sexo in 'fF':
        cadastro['sexo'] = sexo
        break
    else:
        print('opção inválida!')
cadastro['idade'] = int(input('Idade: '))
user.append(cadastro.copy())
while True:
    op = input('Quer continuar? [S/N]')
    if op in 'nN':
        break
    elif op in 'sS':
        cadastro['nome'] = input('Nome: ')
        while True:
            sexo = input('Sexo: [M/F]')
            if sexo in 'mM' or sexo in 'fF':
                cadastro['sexo'] = sexo
                break
            else:
                print('opção inválida!')
        cadastro['idade'] = int(input('Idade: '))
        user.append(cadastro.copy())
    else:
        print('opção inválida!')

print('-='*30)

numPessoas = len(user)
print(f'(A) Ao todo temos {numPessoas} pessoas cadastradas.')

somaIdade = 0
for i in user:
    somaIdade += i['idade']
mediaIdade = somaIdade/numPessoas
print(f'(B) A média de idade é de {mediaIdade} anos.')

print(f'(C) As mulheres cadastradas foram ', end='')
for i in user:
    if i['sexo'] in 'fF':
        print(f', {i["nome"]}', end='')

print(f'\n(D) Lista das pessoas que estão acima da média de {mediaIdade} anos: ')
for i in user:
    if i['idade'] > mediaIdade:
        print(f'    nome = {i["nome"]}; sexo = {i["sexo"]}; idade = {i["idade"]};')

print(f'\nlista de cadastro efetuados: \n{user}')
print('     << ENCERRADO >>')
