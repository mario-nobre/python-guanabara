frase=input('digite uma frase: ').strip().upper()
palavras= frase.split()
junto=''.join(palavras)
#inverso=''

#for x in range(len(junto)-1,-1,-1):   'maneira mais complicada'
 #   inverso += junto[x]
inverso=junto[::-1]
print(junto, inverso)
if junto == inverso:
    print(' é palindromo')
else:
    print('não é palindromo')
