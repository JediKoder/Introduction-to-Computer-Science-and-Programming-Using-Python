# 6.00 Problem Set 3
#
# Hangman game

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    guessed = True
    for char in secretWord:
        if char in lettersGuessed:
            guessed = guessed and True
        else:
            guessed = guessed and False
    return guessed


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedWord = guessedWord + letter + " "
        else:
            guessedWord = guessedWord + "_ "
    return guessedWord[:-1]


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = ''
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    for char in lowercase:
        if char not in lettersGuessed:
            availableLetters = availableLetters + char
    return availableLetters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print "Welcome to the game, Hangman!"
    print "I'm thinking of a word that is " + str(len(secretWord)) + " letters long."
    lettersGuessed = ''
    guessesLeft = 8
    print "------------"
    while True:
        print "You have " + str(guessesLeft) + " guesses left."
        print "Available letters: " + getAvailableLetters(lettersGuessed)
        rawGuess = raw_input("Please guess a letter: ")
        guess = rawGuess.lower()
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed = lettersGuessed + guess
            print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
        elif guess in lettersGuessed:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed = lettersGuessed + guess
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            guessesLeft -= 1
        print "------------"
        if guessesLeft <= 0:
            print "Sorry, You've ran out of guesses. The word was " + secretWord + "."
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print "Congratulations! You've won!"
            break


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
