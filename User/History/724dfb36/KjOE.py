'''
Lista de listas e seus índices
'''
salas = [
    ['maria', 'helena'],
    ['elaine', ],
    ['liuz', 'joao', 'eduarda',(0, 10, 20, 30, 40)],
    
]
# print(salas[0][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])

for i, sala in enumerate(salas):
    for i, aluno in enumerate(sala):
        print( sala)
        print(i, aluno)
