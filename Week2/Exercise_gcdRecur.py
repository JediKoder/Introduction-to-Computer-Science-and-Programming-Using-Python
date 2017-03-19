# Exercise: gcd recur

def gcdRecur(a ,b):
    '''

    :param a, b: positive integers
    :return: a positive integer, the greatest common divisor of a & b.
    '''

    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


# Test


print(gcdRecur(2, 12))
print(gcdRecur(6, 12))
print(gcdRecur(9, 12))
print(gcdRecur(17, 12))