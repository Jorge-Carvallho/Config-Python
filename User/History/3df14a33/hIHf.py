'''
Exercício
Crie funções que duplicam, triplicam, e qudruplicam
o número recebido como parametro
'''
# ==========================
# def duplicar(numero):
#     return numero * 2
# def triplicar(numero):
#     return numero * 3
# def quadruplicar(numero):
#     return numero * 4


# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))
# =============================


# ===========================================
# def criar_multiplicador(multiplicador):
#     def multiplicar(numero):
#         return numero * multiplicador
#     return multiplicar
    
    
# duplicar = criar_multiplicador(2)
# triplicar= criar_multiplicador(3)

# print(duplicar(2))
# print(triplicar(2))
# ++++++++++++++++++++++++++++++++++++++++

def criar_potencia(expoente):
    def potencia(numero):
        return numero ** potencia
    return potencia

    
quadrado = criar_potencia(2)
cubo = criar_potencia(3)

print(quadrado(4))
print(cubo(2))

