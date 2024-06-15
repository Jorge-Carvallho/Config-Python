"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '746.824.890-70' # cpf string recebido pelo usuario

cpf_limpo = cpf.replace('.','').replace('-','') # cpf retirado . e - 
cpf_int = int(cpf_limpo) # cpf limpo convertido de string para numero inteiro


nove_digitos = cpf_limpo[:9] #pegando apenas os 9 primeiros digitos para calculo
contador_regressivo_1 = 10 # contador usado a frente para a multiplicacao
resultado_digito_1 = 0 # resultado sera gerado depis do calculo multiplicado e somado

for digitos in nove_digitos:
    # print(f'{digitos} {contador_regressivo}' ) 
    resultado_digito_1 += (int(digitos) * contador_regressivo_1) # aqui é gerado o primeiro digito do calculo digitos * contador regressivo em ordem decrecente e ja somado cada resultado da multiplicacao mas soma dos resultados 1 a 1 ex... 1* 10 = 10 | 2*10 = 20 mas 10 =30
    print(f'{digitos} * {contador_regressivo_1} += {resultado_digito_1}  ')
    digito_1 = (resultado_digito_1 * 10) % 11
    contador_regressivo_1 -= 1
    
    digito_1 = digito_1 if digito_1 <= 9 else 0
print(f'Primeiro digito gerado é {digito_1}')