'''
Desempacotamento em chamadas
de métodos e funçoẽs
'''
string = 'ABCD'
lista = ['Maria', 'Helena', 1,2,3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# a,b,c ,*_ = lista
# print(a,c,)

for i, nome in enumerate(lista):
    print(i,nome)