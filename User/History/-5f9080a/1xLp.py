# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
# ====================v=======================
# def multiplicacao(*args):
#     total = 1
#     for numero in args:
#         print(f'Total de {total} * {numero} = {total * numero}' )
#         total *= numero
#         print('total', total)
#     return total

# resultado = multiplicacao(1,2,3,4,5)
# print(resultado)
# =====================^=======================


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
numero = input('Informe um número')

def impar_par(numero):
        
    multiplo_de_dois =  numero / 2 == 0
   
    if multiplo_de_dois:
        return 'par'
    else:
        return 'impar'
    
impar_par(numero)

