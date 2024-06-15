
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
        info = ''