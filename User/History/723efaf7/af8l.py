'''
Iterador -> quem sabe intergar um valor por vez
next     -> me entrega o próximo
iter     -> me entrega o iterador
'''

texto = 'Jorge'    #iteravel

iterador = iter(texto)   # iterador


while True:
    try:
        letra = next(iterador)
        print(letra)
    except:
        ...