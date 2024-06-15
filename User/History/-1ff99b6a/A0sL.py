nome = 'henrique'

# for c in nome:
#     if c =='e' or c =='i' or c =='u':
        
#         print(c.upper())
#     else:
#         print(c)
# acima Mostrara o nome com as vogais  eiu em mauisculos 
# ==========================================================


for c in nome:
    if c in 'aeiou': # se c for vogal converte para maiuscula
        print(c.upper())
    elif c == 'q': # senao se c for q converte para @
        print('@') 
    else:
        print(c) # se nao imprima normal