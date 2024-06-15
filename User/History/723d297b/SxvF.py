string = 'qualquer valor'

i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break
    
    print(letra)
else:
    print('Nao econtrei um espaço na string')

print('Fora da string')