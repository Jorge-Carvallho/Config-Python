# row = 'Henrique', 'Noterói', 22.9, 43.1

# def f(t):
#     nome, *meio, long = t
#     print(nome, long, meio )
    
    
# if __name__ == '__main__':
#     f(row)
# ========================================================
# exemplo 2

# row = 'jorge', 'salvador', 30.3, 18.5

# def f(t):
#     nome, *_, long = t
#     print(nome, long, _, _) 
    
# if __name__ == '__main__':
#     f(row)
# ==============================================================
# exemplo3

row = 'lais', 'pernanbuco', 30.2, 22.2

def f(t):
    *resto, _, lat, long = t
    print(lat, long, _)
    
if __name__ == '__main__':
    f(row)
