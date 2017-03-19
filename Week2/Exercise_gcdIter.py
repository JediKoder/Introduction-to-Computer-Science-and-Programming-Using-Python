# Exercise: gcd iter

def gcdIter(a, b):
    '''

    :param a, b: positive integers
    :return: a positive integer, the greatest common divisor of a & b.
    '''

    test = min(a, b)

    while test > 1:
        if a % test == 0 and b % test == 0:
            return test
        else:
            test -= 1

    if test == 1:
        return 1


# Test:

print(gcdIter(17, 12))
