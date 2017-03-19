# Write a Python function that returns the sum of the pairwise products of listA and listB.
# You should assume that listA and listB have the same length and are two lists of integer numbers.
# For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is 1*4 + 2*5 + 3*6,
# meaning your function should return: 32

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    ans = 0

    for idx in range(len(listA)):
        ans += listA[idx] * listB[idx]

    return ans

# Unit Test
print(dotProduct([1, 2, 3], [4, 5, 6]))
print(dotProduct([-74, -59, 74, -18, -16, 8, 86], [-71, -61, -80, -83, 50, -56, 94]))
print(dotProduct([100, 11, 97], [-58, -40, 98]))