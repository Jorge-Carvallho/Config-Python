def soma(*args):
    total = 0
    for numero in args:
        total += numero
        print(total)
    return total
        

soma_1_2_3 = soma(1,2,3)
soma(1,2,3)
print


# passar uma quantidade de argumentos ilimitados de soma não nomeados