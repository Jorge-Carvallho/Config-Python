# nome = input('Digite seu nome ')
# idade = input('Digite sua idade ')
nome = 'jorge Carvalho'
idade = 34


if nome ==nome and idade == idade:
    print(f'Seu nome é {nome} e idade é {idade}')
    print(f'Meu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Meu nome comtem espacos')
    else:
        print('Meu nome nao cotem espaços')
        
    print(f'Meu nome contem {len(nome)} letras')
    print(f' A primeira letra do meu nome é {nome[0]}')
    print(f'A última letra do meu nome é {nome[-1]} ')
else:
    print('Voce deixou campos vazios')