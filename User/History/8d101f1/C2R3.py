
primeiro_valor = input('Digite o primeiro valor')
segundo_valor = input('Digite o segundo valor')

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

if int_primeiro_valor > int_segundo_valor:
    print(f'O primeiro valor  {int_primeiro_valor } é maior que o segundo {int_segundo_valor}')
elif int_primeiro_valor < int_segundo_valor:
    print(f'O primeiro Valor é {int_primeiro_valor} é menor que o segundo valor {int_segundo_valor}')
else:
    print(f'Ambos os valores {int_primeiro_valor} e {int_segundo_valor} são iguais')