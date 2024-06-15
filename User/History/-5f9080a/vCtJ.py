


def multiplicacao(*args):
    total = 1
    for numero in args:
        print('total de ', numero, '*', numero )
        total *= numero
        print('total', total)
    return total

# resultado = multiplicacao(1,2,3,4,5)
# print(resultado)

