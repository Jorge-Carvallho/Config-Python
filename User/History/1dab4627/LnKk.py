'''
args - argumentos não nomeados
* - *args(empacotamento e desempacotamento)

'''
#Lembre de desempacotamento

x,y,*resto = 1,2,3,4

print(resto, x,y)
print(x,y,resto)
print(x,resto,y)
