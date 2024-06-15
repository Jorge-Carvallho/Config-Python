
frase = ' O python é uma linguagem de programação'\
        'multiparadigma.'\
        'Python foi criado por Guido Van Rossum.'

i = 0

qtd_apareceu_mas_vezes = 0
letra_apareceu_mas_vezes = ''

while i < len(frase):
        letra_atual = frase[i]
        qtd_apareceu_mas_vezes_atual = frase.count(letra_atual)
        i += 1
        
        if qtd_apareceu_mas_vezes < qtd_apareceu_mas_vezes_atual:
           qtd_apareceu_mas_vezes = qtd_apareceu_mas_vezes_atual
           letra_apareceu_mas_vezes = letra_atual
        
        
    print('A letra que apareceu mas vezes foi'
           f'{letra_apareceu_mas_vezes} que apareceu'     
           f'{qtd}'

)