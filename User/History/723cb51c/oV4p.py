# Calculadora com while
while True:
    numero_1 = input('Digite um número ')
    numero_2 = input('Digite outro número ')
    operador = input('Digite o operador (+-*/): ')
    
    numero_validos = None
    
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_validos = True
    except :
        numero_validos = None
      
    if numero_validos is None:
        print('algum Número inválido')
        continue
    
    operadores_permitidos = '+-*/'
    
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue


    
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    
 
 
    
    sair = input('Deseja sair? [s]im:').lower().startswith('s')

    if sair is True:
        print(sair)
        break