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
