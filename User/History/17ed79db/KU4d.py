'''
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o memso valor na memória (mutével)
'''

# nome = 'luis'

# nome = 'João'

# print(nome)
# =============================

lista_a = [ 1,234,'jorge']

lista_b = lista_a
lista_a[2] = 'jorge miranda'
lista_b[2] = 123
print(lista_b, lista_a)