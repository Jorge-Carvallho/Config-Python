"""
Flag (Bandeira) - Marca um local
None = Nao valor
is e is not + é ou nao é (tipo, valor, identidade)
id = Identidade
"""


condicao =  False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faça algo')
else:
    print('Não faça algo')
    
    
print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None) # is not  o mesmo de negaçao