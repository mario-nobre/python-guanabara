nota1=float(input('primeira nota: '))
nota2=float(input('segunda nota: '))
media=(nota1+nota2)/2
print('tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1,nota2,media))
if 7 > media >= 5:
    print('o aluno está em recuperação.')
elif media <5:
    print('o aluno está reprovado.')
else:
    print('o aluno está aprovado.')
