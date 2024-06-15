# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'jorge carvalho',
    'sobrenome': 'miranda',
    int(22): 'hf'
    
}
# print(pessoa.__len__())
# print(len(pessoa)) #retorna qiuantidade de uma chave
# ----------------------------------------------------------
# print(pessoa.keys())# return count de keys
# print(list(pessoa.keys()))# return keys in list
# print(tuple(pessoa.keys()))#return keys in tuple
# for chave in pessoa.keys():# return keys in count in for
#     print(chave)
# -----------------------------------------------------------
# print(list(pessoa.values()))#return values's keys
# for valor in pessoa.values():# return values in count in for
#     print(valor)
# ------------------------------------------------------------
# print(list(pessoa.items())) #return keys and values in tuple
# for chave, valor in pessoa.items():
#     print(chave, valor)
