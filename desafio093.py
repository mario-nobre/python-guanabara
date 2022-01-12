dados = {'nome': input("Nome do jogador: ")}
partidas = int(input('Quantas partidas ' + dados['nome'] + ' jogou? '))
gol = []
for i in range(0, partidas):
    listaGol = int(input(f'   Quantos gols na partida {i+1}? '))
    gol.append(listaGol)
dados['gols'] = gol
dados['total'] = sum(gol)
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for i, j in enumerate(gol):
    print(f'    => Na partida {i+1}, fez {j} gols.')
print(f'Foi um total de {dados["total"]} gols.')
