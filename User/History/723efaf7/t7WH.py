'''
Iterador -> quem sabe intergar um valor por vez
next     -> me entrega o próximo
iter     -> me entrega o iterador
'''

texto = 'Jorge'
iterador = iter(texto)   # iterador


# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
       
#     except StopIteration:
#         break

# criado abaixo é o mesmo que criado a cima com iterador ciado na unha :

for letra in texto:
    print(letra)
