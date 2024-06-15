'''
enumerate - enumera iteraveis (indices)

'''
lista = ['maria', 'jorge', 'luiz']
lista.append('joao')

lista_enumerada = enumerate(lista) #  enumerate em uma variada é comsumida toda de uma vez, ultilizar da forma abaixo
print(lista_enumerada)
for item in lista_enumerada:
    print(item)