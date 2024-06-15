'''
split e join com list e str
split - divide uma string
join - une uma string
rstrip - corta os espacos da direita
lstrip - corta os espacos da esquerda
'''
# frase = 'Olha so que, coisa interesante'
# lista_palavras = frase.split()
# print(lista_palavras)
# ========================================

# frase = 'o tempo disse para o tempo, que todo com tempo tem tempo'
# lista_de_frases = frase.split(', ')

# for i, frase in enumerate(lista_de_frases):
#     print(lista_de_frases[i])
# ==============================================

frase = 'O       temo disse         para o tempo,      que todo comtempo tem tempo'

lista_de_frases_cruas = frase.split()
print(lista_de_frases_cruas)