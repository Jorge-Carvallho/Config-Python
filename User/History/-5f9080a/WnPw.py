


def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
        print(numero)
    return total

resultado = multiplicacao(1,2,3,4,5)
print(resultado)
