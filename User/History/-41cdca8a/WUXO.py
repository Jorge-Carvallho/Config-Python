'''
Higher Order Functions - Funções de ordem superior
Funçoes de primeira classe
'''
def saudacao(msg):
    return msg
saudacao_2 = saudacao # apontando uma variavel de fora pra a variavel da função
print(saudacao('Bom dia'))