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
            inf0 = f''