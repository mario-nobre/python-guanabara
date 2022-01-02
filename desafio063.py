print('-'*30)
print('sequência de fibonacci')
print('-'*30)
num=int(input('quantos termos você que mostrar? '))
primeiro = 0
segundo = 1
termo=3
if num == 1:
    print(primeiro, '-', end=' ')
else:
    print(primeiro,'-',end=' ')
    print(segundo,'-',end=' ')
    while termo <= num:
        proxtermo = segundo + primeiro
        termo = termo + 1
        print(proxtermo,'-',end=' ')
        primeiro = segundo
        segundo = proxtermo
 print('FIM')
 