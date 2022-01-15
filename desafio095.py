from tabulate import tabulate
lista = []
listaAux = []
num = 0
while True:
    jogador = {"cod": num}
    gol = []
    jogador['nome'] = input("Nome do jogador: ")
    partidas = int(input('Quantas partidas ' + jogador['nome'] + ' jogou? '))
    for i in range(0, partidas):
        listaGol = int(input(f'   Quantos gols na partida {i + 1}? '))
        gol.append(listaGol)
    jogador['gols'] = gol
    jogador['total'] = sum(gol)
    lista.append(jogador)

    listaTemp = []
    for i in jogador.values():
        listaTemp.append(i)
    listaAux.append(listaTemp)

    while True:
        op = input('quer continuar? [S?N] ')
        if op in 'nN':
            break
        elif op in 'sS':
            num += 1
            break
        else:
            print('Digite uma opção válida')
    if op in 'nN':
        break

print('-='*30)
print(tabulate(listaAux, headers=["cod", "nome", "gols", "total"]))

while True:
    numJogador = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if numJogador == 999:
        print('     --   ENCERRADO   --')
        break
    elif numJogador < 0 or numJogador >= len(lista):
        print("Digite um valor válido.")
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[numJogador]["nome"]}: ')
        for i, j in enumerate(lista[numJogador]["gols"]):
            print(f'    No jogo {i+1} fez {j} gols.')
