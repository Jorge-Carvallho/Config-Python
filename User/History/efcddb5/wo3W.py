
def donuts(count):
    if count >= 10:
        return 'Number of donuts: many'
    else:
        return f'Number of donuts: {count}'
    
    
def test(f, in_, expected):
    
    out = f(in_)

    if out == expected:
        sign = 'OK'
        info = ''
    else:
        sign = 'NOT'
        info = f'e o correto é {expected!r}'
    
    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')
    
if __name__ == '__main__':
    test(donuts, 4, 'Number of donuts: 4')
    test(donuts, 9, 'Number of donuts: 9')
    test(donuts, 10, 'Number of donuts: many')
    test(donuts, 99, 'Number of donuts: many')