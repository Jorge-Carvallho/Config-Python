'''
Closure e funções que retoman outras funções
'''
def criar_saudacao(saudacao,nome):
    def saudar():
        return f'{saudacao} {nome}'
    return saudar


s1 = criar_saudacao('Bom dia', 'luiz')
s2 = criar_saudacao('Boa noite', 'joao')

print(s1())
print(s2())