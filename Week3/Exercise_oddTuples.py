#Exercise: odd tuples
#Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output,
# where every other element of the input tuple is copied, starting with the first one.
# So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'),
# then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    oddTuple = ()

    for element in range(0, len(aTup), 2):
        oddTuple += aTup[element],

    return oddTuple

# Test Case

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
print(oddTuples(()))
print((oddTuples((4,))))
print((oddTuples((12, 13, 4, 3, 17, 20, 12, 15, 16, 3))))
