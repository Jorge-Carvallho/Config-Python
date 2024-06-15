
primeiro_valor = input('Digite o primeiro valor')
segundo_valor = input('Digite o segundo valor')

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

if int_primeiro_valor > int_segundo_valor:
    print('O primeiro valor é maior que o segundo')
elif int_primeiro_valor < int_segundo_valor:
    print('O primeiro Valor é menor que o segundo valor')
else:
    print('Ambos os valores são iguais')