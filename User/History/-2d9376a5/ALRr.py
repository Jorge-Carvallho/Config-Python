row = 'Henrique', 'Noterói', 22.9, 43.1

def f(t):
    nome, *_, long = t
    print(nome, long, _)
    
    
if __name__ == '__main__':
    f(row)