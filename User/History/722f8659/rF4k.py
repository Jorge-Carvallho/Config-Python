"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# entrada = input('Digite um número ')
# if entrada.isdigit():
#     numero_int = int(entrada)
#     if numero_int % 2 == 0:
#         print('número par')
#     else:
#         print('número impar')
        
# else:
#     print('Entrda invalida, digite uam entrada valida')
            
        
        
    





"""
Faça um programa que exige a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação correspondente. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora = input('Digite a Hora (0-24): ')
# if hora.isdigit():
#     hora_int = int(hora)
#     if 0 <= hora_int < 24:
#         if 0 <= hora_int < 12:
#             print('bom dia')
#         elif 12 <= hora_int < 18:
#             print('Boa tarde')
#         else:
#             print('boa noite')
#     else:
#         print('digite uam hora valida')
# else:
#     print('Entrada invalida, digite um numero correto')

#codigo2

# entrada = input('Digite a hora em número ')

# try:
#     hora = int(entrada)
#     if hora >= 0 and hora <=12:
#         print('Bom dia')
#     elif hora > 12 and hora <=18:
#         print('Boa tarde')
#     elif hora  > 18 and hora <= 24:
#         print('Boa noite')
#     else:
#         print('Digite apenas entre 0 a 24 horas')

 
# except:
#     print('Digite número inteiro')



"""
Faça um programa que parte do primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
“Seu nome é normal”; maior que 6 escreva "Seu nome é muito grande".
"""
# nome = input('Digite seu nome ')

# if len(nome) <= 4:
#     print('Seu nome é curto')
# elif len(nome) <= 6:
#     print('Seu nome é normal')
# else:
#     print('Seu nome é muito grande')