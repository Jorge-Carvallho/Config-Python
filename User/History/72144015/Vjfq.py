#formatacao e parametro nomeado

a = 'A'
b = 'B'
c = 1.1
string = 'a={nome1} b={nome2} c{nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)
print(formato)
# a,b,c nao argumentos de uma variavel ou resultados passados
#nome1, nome2, nome3 são parâmetro que estão nomeando os argumentos as variaveis ou estão nomeandos os argumentos ja nomedados fora como variaveis 