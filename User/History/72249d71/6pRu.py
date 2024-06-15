"""
Introdução ap try/except
tre -> tentar execultar o codigo
except ->ocorre algum erro ao tentar execultar 
"""
numero_str = input('Dobre o numero digitado: ')

try:
    numero_float = float(numero_str)
    print(f'o dobro de {numero_str} é {numero_float * 2:.0f}'),
except:
    print('incorreto')
    






# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'o dobro de {numero_str} é {numero_float * 2:.0f}'),
# else:
#     print('incorreto')