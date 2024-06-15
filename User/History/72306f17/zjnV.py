'''
Repetição 
While (enquanto)
Execultar uma ação enquanto uma condição for verdadeira
'''

condicao = True

while condicao:
    nome = input('qual seu nome')
    print(f'Nome é {nome}')

    if nome == 'sair':
        break

print('saindo ...')