# Exercise: is In

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''

    if aStr == '':
        return False
    if len(aStr) == 1:
        return char == aStr
    else:
        middle = len(aStr) // 2
        if char == aStr[middle]:
            return True
        elif char > aStr[middle]:
            return isIn(char, aStr[middle+1:])
        else:
            return isIn(char, aStr[:middle])

# Test Cases

print(isIn('a', ''))
print(isIn('a', 'b'))
print(isIn('a', 'ab'))
print(isIn('e', 'abcde'))



