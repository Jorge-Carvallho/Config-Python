'''
Repetição 
While (enquanto)
Execultar uma ação enquanto uma condição for verdadeira
'''

qtd_linha = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linha:
    colunas = 1
    while colunas <= qtd_colunas:
        colunas += 1
    print(f'{linha=}, {colunas=}')
    linha += 1


    