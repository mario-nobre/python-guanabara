nome=input('digite seu nome ').lower().strip()
print('olá! prazer em lhe conhecer.')
lista=nome.split()
print('seu primeiro nome é',lista[0])
seg=len(lista)-1
print('e o seu último nome é',lista[seg])
#print(lista[-1]) outra forma de obter o ultimo
