'''
Introdução ao desempacotamento 
'''
# nome1, *resto =['jorge', 'miranda', 'evandro']

# print(nome1, resto)
# resto.append('igor')
# print(type(resto))
# =========================================

nome1, *_ = ['jorge', 'miranda', ' furico']
print(nome1)