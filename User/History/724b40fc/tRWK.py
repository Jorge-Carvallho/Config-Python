'''
Introdução ao desempacotamento + tuples (tuplas)
'''
nome1, *resto =['jorge', 'miranda', 'evandro']

print(nome1, resto)
resto.append('igor')
print(type(resto))

