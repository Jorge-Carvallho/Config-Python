print('funcionou')
def fix_start(s):
    first_char = s[0]
    rest_of_string = s[1:]
    modified_rest = rest_of_string.replace(first_char, '*')
    return first_char + modified_rest


def test(f, in_, expected):
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f' e o correto é {expected!r}'

    print(f'{sign} {f.__name__} ({in_!r}) retornou {out!r} {info}')


    if __name__ == '___main__':
        test(fix_start, 'babble', 'ba**le')
        test(fix_start, 'aardvark', 'a*rdv*rk')
        test(fix_start, 'google', 'goo*le')
        test(fix_start, 'donuts', 'donut')
        test(fix_start, 'amazonia', 'am*zoni*')
