# Write a function called dict_interdiff that takes in two dictionaries (d1 and d2).
# The function will return a tuple of two dictionaries: a dictionary of the intersect of d1 and d2 and
# a dictionary of the difference of d1 and d2, calculated as follows:
# If f(a, b) returns a + b
# d1 = {1:30, 2:20, 3:30, 5:80}
# d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
# then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
# If f(a, b) returns a > b
# d1 = {1:30, 2:20, 3:30}
# d2 = {1:40, 2:50, 3:60}
# then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    ans = ()
    dIntersect = {}
    dDiff = {}

    for key, value in d1.items():
        if key in d2:
            dIntersect[key] = f(value, d2[key])
        else:
            dDiff[key] = value

    for key, value in d2.items():
        if key not in d1:
            dDiff[key] = value

    ans = dIntersect, dDiff

    return ans

