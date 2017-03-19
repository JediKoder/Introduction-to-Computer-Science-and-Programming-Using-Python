# Problem 9
# Write a function to flatten a list. The list contains other lists, strings, or ints.
# For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    bList = []

    for item in aList:
        if not isinstance(item, list):
            bList.append(item)
        else:
            bList += flatten(item)

    return bList

# Unit Test
print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))