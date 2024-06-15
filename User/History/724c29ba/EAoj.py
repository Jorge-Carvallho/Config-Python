'''
enumerate - enumera iteraveis (indices)

'''
lista = ['maria', 'jorge', 'luiz']
lista.append('joao')

# lista_enumerada = enumerate(lista) #  enumerate em uma variada é comsumida toda de uma vez, ultilizar da forma abaixo
# print(lista_enumerada)#  enumerate em uma variada é comsumida toda de uma vez, ultilizar da forma abaixo
# for item in lista_enumerada:#  enumerate em uma variada é comsumida toda de uma vez, ultilizar da forma abaixo
#     print(item)#  enumerate em uma variada é comsumida toda de uma vez, ultilizar da forma abaixo

for item in enumerate(lista):
    print(item)
