'''
Higher Order Functions - Funções de ordem superior
Funçoes de primeira classe
'''
# def saudacao(msg):
#     return msg
# saudacao_2 = saudacao # apontando a variavel de fora pra a variavel da função
# print(saudacao_2('Bom dia'))


nome_informado = input('informa o nome da pessoa ')
def saudacao(msg):
    return msg

def pessoa(nome):
   return saudacao(nome)

print(nome_informado, 'Bom dia')