def fix_start(s):
    first_char = s[0]
    rest_of_string = s[1:]
    modified_rest = rest_of_string.replace(first_char,'*')
    return first_char + modified_rest

def test(f, in_, expected):
    out = f(in_)

    if out == expected:
        sign