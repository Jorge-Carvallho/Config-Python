'''
Higher Order Functions - Funções de ordem superior
Funçoes de primeira classe
'''
# def saudacao(msg):
#     return msg
# saudacao_2 = saudacao # apontando a variavel de fora pra a variavel da função
# print(saudacao_2('Bom dia'))


nome_informado = input('informa o nome da pessoa ')
hora_informada  = int(input('Informa a hora atual (0 - 23)'))
def saudacao(msg):
    return msg

def pessoa(nome, hora):
    if hora < 12:
        return saudacao 'Bom dia'
    elif <= 12 hora < 18:
        return saudacao 'Boa tarde '
    
   return saudacao 'Boa noite'

print('Bom dia', nome_informado)
