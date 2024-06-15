'''
Valores padrão para parâmetros
Ao definit uma função, os parâmetros podem 
ter valores padrão. Caso o valor não seja
enviadopara p parâmetro, o valor padrão será 
usado
Refatorar: editar seu código
'''

def soma (x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x y, z)
    else:
        print(f'{x=} {y}', x + y +z)
    

soma(2,1)
soma(3,5)
soma(1,2,3)