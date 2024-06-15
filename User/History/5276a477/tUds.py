'''
Closure e funções que retoman outras funções
'''
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao} {nome}'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia', 'luiz')
falar_boa_noite = criar_saudacao('Boa noite', 'joao')

print(s1())
print(s2())