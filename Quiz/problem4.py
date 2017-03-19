def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    val = 0
    while True:
        val += 1
        if 0 < x - b**val < b:
            return val
