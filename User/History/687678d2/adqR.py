lista = []

while True:
    print('Selecione uma opção')
    valor = input('[i]Inserir [a]Apagar [l]Listar ')
    
    if valor == 'i':
        valor = input('digite o item: ')
        lista.append(valor)
        print(lista)

    if valor == 'a':
        ...
        
    if valor == 'l':
        





















































# import os

# lista = []

# while True:
#     print('Selecione uma opção')
#     opcao = input('[i]Inserir [a]apagar [l]listar ')

#     if opcao =='i':
#         os.system('clear')
#         item = input('Item: ', )
#         lista.append(item)
#         # print(lista)
#     elif opcao == 'a':
#         indice_string = input('Escolha o indice para apagar ')

#         try:
#             indice = int(indice_string)
#             del lista[indice]
#             print('Indice', indice, 'apagado')
            
#         except IndexError:
#             print('Não a item com esse indice na lista')
#         except ValueError:
#             print('Digite apenas números inteiros.')
        
        
#     elif opcao == 'l':
#         os.system('clear')
#         if len(lista) == 0:
#             print('Não a item na lista')

#         for i, valor in enumerate(lista):
#             print(i, valor)
        
#     else:
#         print('opção invalida, digite novamente')

   
   