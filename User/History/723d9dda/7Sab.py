
frase = ' O python é uma linguagem de programação'\
        'multiparadigma.'\
        'Python foi criado por Guido Van Rossum.'

i = 0

while i < len(frase):
        letra_atual = frase[i]
        vezes_de_letra_apareceu = frase.count(letra_atual)
        print(letra_atual, vezes_de_letra_apareceu)
        i += 1