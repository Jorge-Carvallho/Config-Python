def soma(*args):
    total = 0
    for numero in args:
        total += numero
        # print(total)
    return total
        

soma_1_2_3 =soma(1,2,3)
print(soma_1_2_3)
soma_4_5_6 =  soma(4,5,6)
print(soma_4_5_6)
soma_de_len = soma(len.str('jorge'))


# passar uma quantidade de argumentos ilimitados de soma não nomeados