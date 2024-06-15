'''
Exercício
Crie funções que duplicam, triplicam, e qudruplicam
o número recebido como parametro
'''
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar
    
    
duplicar = criar_multiplicador(2)
triplicar= criar_multiplicador(3)

print(duplicar(2))
print(triplicar(2))