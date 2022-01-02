nome=input('qual o seu nome completo? ')#use como exemplo;      Mario dos Santos Nobre.
print(nome.upper())#transforma em maiúsculas.
print(nome.lower())#transforma em minúsculas.
print(nome.capitalize())#coloca o primeiro caractere em maiúscula e o restante em minúsculo.
print(nome.title())#capitaliza todas as palavras na variável.
print(len(nome))#conta quantos caracteres possui a variável, incluindo os espaços.
print(nome.strip())#remove os espacos a direita e esquerda da variável.
print(nome.count('os'))#conta a repetição do valor pedido dentro da variável.
print(nome[1:16:2])#fatia o valor da variável ate o espaço 16 em dois em dois.
print(nome.find('os'))#em qual posição ele encontra o valor pedido dentro da variável.('-1'=não encontrado.)
print('dos' in nome)#verifica se é verdadeiro ou falso o termo procurado detro da variável.
print(nome.replace('dos Santos','Doutor'))#troca o termo procurado por outro.
nomesep=nome.split()#divide o texto considerando os espaçoas como divisores. cria uma 'lista' deles.
print(nomesep)#necessário criar variável antes para usar função 'join'.
print('-'.join(nomesep))#faz a junção dos elementos dentro da lista de uma variável.''=elimina os espaços.
