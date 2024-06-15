def both_ends(s):
    if len(s) < 2:
        return ''
    else:
        return s[:2] + [2:]
    