def fix_start(s):
    first_char = s[0]
    rest_of_string = s[1:]
    modified_rest = rest_of_string.replace(first_char,'*')
    return