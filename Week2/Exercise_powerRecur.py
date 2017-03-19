# Exercise: Power Recursive

def recurPower(base, exp):
    '''

    :param base: int or float
    :param exp: int >= 0
    :return: int or float, base^exp
    '''

    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recurPower(base, exp-1)


# Test
print(recurPower(2, 8))