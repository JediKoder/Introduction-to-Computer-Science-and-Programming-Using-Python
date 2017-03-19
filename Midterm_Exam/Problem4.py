# Problem 4

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    num = int(num)
    temp_diff = num
    exp_final = 0

    for exponent in range(num):
        diff = abs(base**exponent - num)
        if diff < temp_diff:
            temp_diff = diff
            exp_final = exponent

    return exp_final





# Unit Tests
print(closest_power(4,1)) # returns 0
print(closest_power(3,12)) # returns 2
print(closest_power(4,12)) # returns 2
print(closest_power(2, 192.0))
print(closest_power(5, 375.0))
print(closest_power(10, 550.0))