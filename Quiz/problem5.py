def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.

    For example, if we lace 'abcd' and 'efghi',
    we would get the new string: 'aebfcgdhi'.

    """
    laces = ''
    for i in range(min(len(s1), len(s2))):
        laces = laces + s1[i] + s2[i]
    if len(s1) != len(s2):
        if len(s1) > len(s2):
            laces = laces + s1[-(len(s1)-len(s2)):]
        else:
            laces = laces + s2[-(len(s2)-len(s1)):]
    return laces
