'''
Higher Order Functions - Funções de ordem superior
Funçoes de primeira classe
'''
# def saudacao(msg):
#     return msg
# saudacao_2 = saudacao # apontando a variavel de fora pra a variavel da função
# print(saudacao_2('Bom dia'))

def saudacao(msg):
    return msg

def pessoa(nome):
   return saudacao(nome)


print(pessoa('jorge', 'Bom dia'))
