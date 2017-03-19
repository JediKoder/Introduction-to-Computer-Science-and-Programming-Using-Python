# Exercise: biggest

def biggest(aDict):
    '''

    :param aDict: A dictionary, where all the values are lists.
    :return: The key with the largest number of values associated with it.
    '''

    big = 0
    big_key = ''

    for key, values in aDict.items():
        if len(values) > big:
            big = len(values)
            big_key = key

    return big_key





# Test Cases
animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}

print(biggest(animals))