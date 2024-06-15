'''
Operação ternária (condicional de uma linha)
< valor - if - <condicional> else <outro valor>
'''
# exemplo
# print('Valor' if True else 'outro valor')
# print('Valor' if False else 'outro valor')
# =======================================================

# condicao = 10 == 10

# variavel = print('valor correto ' if condicao else 'Valor incorreto')
# =========================================================

digito = input('Digite o  digito cpf')

novo_digito = digito if digito <= 9 else 0
print(novo_digito)