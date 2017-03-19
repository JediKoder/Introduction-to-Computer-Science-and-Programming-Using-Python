def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    return char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or \
        char.lower() == 'o' or char.lower() == 'u'
