import decimal

# o importe decimal funcina melhor para numeros float muito fgrande

numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2




print(numero_3)
print(f'{numero_3:.2f}') # formate ele formata a string em float adicionando as casas decimais

print(round(numero_3,1)) # round ele arredonda o valor para float sem as proximas casas decimais