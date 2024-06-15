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
print(y)
def escopo():
    global x
    x = 111
    print(f'{x} aqui ele muda e continua com valor mudado')
    def outra_funcao():
        global y
        y = 9
        print(x,y)
        print(y)


    
        outra_funcao()
    print(f'{x} {y} print da ')

    print(f'{y} de y')

print(f'{x} aqui 1')



escopo()


print(f'{x} aqui ele finaliza coma variavel alterada')