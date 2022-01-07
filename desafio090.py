nome = input("Nome: ")
media = float(input(f'Média de {nome}: '))
aluno = {'nome': nome, 'media': media}
print("=-"*50)
if aluno['media'] >= 7:
    aluno['status'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['status'] = 'RECUPERAÇÃO'
else:
    aluno['status'] = 'REPROVADO'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
