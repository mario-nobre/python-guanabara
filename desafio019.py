a1=input('digite o nome do aluno 1 ')
a2=input('digite o nome do aluno 2 ')
a3=input('digite o nome do aluno 3 ')
a4=input('digite o nome do aluno 4 ')
lista=[a1,a2,a3,a4]
import random
print()
s=random.choice(lista)
print('o escolhido é o aluno,{}'.format(s))
