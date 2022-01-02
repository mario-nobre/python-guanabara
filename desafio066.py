cont = soma = 0
while True:
    op=int(input('digite um valor '))
    if op == 999:
        break
    cont += 1
    soma += op
print(f'a soma dos {cont} valores foi {soma}!')
