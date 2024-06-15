def both_ends(s):
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[2:]
    
def test(f, in_, expected):
        
        out = f(in_)
        
        if out == expected:
            sidn = '✅'
            info = ''
        else:
            sign = '❌'
            inf0 = f'e o correto é {expected!r}'
        print(f'{sign} {f.__name__} ({in_!r}) retornou {out!r} {info}')

if __name__ =='__main__':
    test(both_ends, 'spring', spng)
    test(both_ends, 'hello', 'helo')
    test(both_ends, 'a', '')
    test(both_ends, 'xyz', 'xyyz')