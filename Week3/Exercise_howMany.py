# Exercise: how many

def how_many(aDict):
    '''

    :param aDict: A dictionary, where all the values are lists.
    :return: int, how many values are in the dictionary.
    '''
    items = list(aDict.values())
    total = 0
    for item in items:
        assert isinstance(item, object)
        total += len(item)

    return total





# Test Cases
animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}

print(how_many(animals))