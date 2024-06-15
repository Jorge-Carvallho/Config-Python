lista = ['maria', 'helena', 'luiz']
indice = 0
lista.append([True])
lista.extend([2,32,False])

for nome in lista:
    print(indice, lista[indice], type(nome))
    indice += 1