nome = 'henrique'

# for c in nome:
#     if c =='e' or c =='i' or c =='u':
        
#         print(c.upper())
#     else:
#         print(c)
# acima Mostrara o nome com as vogais  eiu em mauisculos 
# ==========================================================


for c in nome:
    if c in 'eiu':
        print(c.upper())
    else:
        print()