''' dados = {"nome": "pedro", "idade": 25}
print(dados)
dados["sexo"] = "masculino"
print(dados)
print(dados["nome"])
print(dados["idade"])
print(dados["sexo"])
del dados["idade"]
print(dados)


filme = {"titulo": "star wars",
         "ano": 1977,
         "diretor": "george lucas"}

for k, v in filme.items():
    print(f'O {k} é {v}')
    '''

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = input('unidade federativa')
    estado['sigla'] = input('sigla do estado')
    brasil.append(estado.copy())
print(brasil)
