# Calculadora com while
while True:
    numero_1 = input('Digite um número')
    numero_2 = input('Digite outro número')
    operador = ('Digite o operador (+-*/):')
    
    numero_validos = None
    
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_validos = True
    except :
        ...
 
 
 
 
    
    sair = input('Deseja sair? [s]im:').lower().startswith('s')

    if sair is True:
        print(sair)
        break