def soma(*args):
    total = 0
    for numero in args:
        total += numero
        print(total)

soma(1,2,3,4,5,6)


# passar uma quantidade de argumentos ilimitados de soma 