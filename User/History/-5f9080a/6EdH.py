


def multiplicacao(*args):
    total = 0
    for numero in args:
        total += numero
    return total

resultado = multiplicacao(1,2,3,4,5)
print(resultado)