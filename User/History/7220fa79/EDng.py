# #Operadores Lógicos   AND
# and(e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso,
# a expressão inteira sera avaliada naquele valor
# 0 0.0 '' falso
# Também existe tipo None que é usado para representar um não valor


entrada = input('[E]ntrar [S]air ')
senha_digitada = input('Senha ')
senha_permitida = '12345'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('entrada permitida')
else:
    print('saindo...')