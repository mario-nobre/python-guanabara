casa=float(input('qual o valor da casa?: R$ '))
salario=float(input('qual o valor do seu salário? R$ '))
anos=int(input('em quantas anos você quer pagar?'))
mensalidade=casa/(anos*12)
print('prestação será de: R$',mensalidade)
if mensalidade > 0.3*salario:
    print('emprestimo negado')
else:
    print('emprestimo aprovado')
