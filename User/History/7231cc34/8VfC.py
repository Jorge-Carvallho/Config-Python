contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Nao vou mostrar o numero 6.')
        continue

    if contador >= 10 and contador <= 27:
        print(f'Não irei mostrar {contador}')
        
    print(contador)
    
    if contador == 40: 
    
    break