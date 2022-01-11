from datetime import datetime

dados = {}
dados['nome'] = input("Nome: ")
nasc = int(input("Ano de Nascimento: "))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input("Carteira de Trabalho?(0-não tem: "))

if dados['ctps'] == 0:
    print('=-' * 30)
    for k, v in dados.items():
        print(f'- {k} tem o valor {v}')
else:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário R$: '))
    aposento = (dados['contratação'] + 35) - nasc
    dados['aposentadoria'] = aposento
    print('=-' * 30)
    for k, v in dados.items():
        print(f'    - {k} tem o valor {v}')
