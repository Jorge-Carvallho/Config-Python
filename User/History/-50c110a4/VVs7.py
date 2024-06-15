'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e local
O escopo global é o escopo onde todo o código é alcançavel
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados
'''

# x = 1

# def escopo():
#     x = 10
#     print(x)
#     def outra_funcao():
#         y = 2
#         print(x,y)


    
#     outra_funcao()
#     print(x)


# print(x)

# escopo()
# print(x)

# ==================================================
# permitindo que o x fosse editado dentro da funcao

x = 1
y=3
print(' saida 01',x)
print('saida 02',y)
def escopo():
    global x
    x = 111
    print(f'{x} aqui ele altera e continua com valor mudado')
    
    def outra_funcao():
        global y
        y = 9
        print(f'{x} {y} esses x e y estão da outra função')
        print(f'{y} este y aqui esta dnetro da outra função')
            
    


print(f'{x}  aqui o x de fora da funcao valor 1')



escopo()


print(f'{x} aqui ele finaliza coma variavel alterada')
    
    # def outra_funcao():
    #         global y
    #         y = 9
    #         print(x,y)
    #         print(y)
    # print(f'{y} de y')
    # outra_funcao()
    # print(f'{x} {y} print da ')
