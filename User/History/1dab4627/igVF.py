'''
args - argumentos não nomeados
* - *args(empacotamento e desempacotamento)

'''
#Lembre de desempacotamento

x,y,*resto = 1,2,3,4,5,6,7

print(resto, x,y)
print(x,y,resto)
print(x,resto,y)


def soma(x,y):
    return x + y

print(1,2,3,4,5)
soma(2,3)