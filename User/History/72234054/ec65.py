"""
Formatação básica de strings
s - corda
d-int
f - flutuar
.<número de dígitos>f
x ou X - Hexadecimal
(Caracteres)(><^)(quantidade)
> - Esquerda
< - Direita
^ -Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Sinalizadores de conversão - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.')# 10 casas deciamis pra esquerda
print(f'{variavel: <10}.')#10 casas decimais a direita
print(f'{variavel:}')