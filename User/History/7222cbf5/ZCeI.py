# Interpolação basica de strings
# s - string
# d e i - int
# f -  float
# x e X - Hexadecimal(ABCDEF0123456789)

nome = 'Luis'
preco = 1000.95897643
variavel = '%s, o preço e R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de nome %d é %X' % (14, 18))