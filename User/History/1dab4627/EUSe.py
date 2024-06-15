'''
args - argumentos não nomeados
* - *args(empacotamento e desempacotamento)

'''
#Lembre de desempacotamento

# x,y,_,_,*resto = 1,2,3,4,5,6,7

# print(resto, x,y)
# print(x,y,resto)
# print(x,resto,y)
# ===============================

# def soma(x,y):
#     return x + y

# print(1,2,3,4,5)
# resultado = soma(2,3)
# print(resultado)
# print(soma(2,3))
# =================================

def soma(*args):# argumentos não nomeados 
    args = list(args)
    args.append(7)
    print(args)
    args = args()

soma(1,2,3,4,5,6)