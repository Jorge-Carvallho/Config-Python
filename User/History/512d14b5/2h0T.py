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
print(pessoa.keys())# return quat de keys
print(list(pessoa.keys()))# return keys in list
print(tuple(pessoa.keys()))#return keys in tuple
