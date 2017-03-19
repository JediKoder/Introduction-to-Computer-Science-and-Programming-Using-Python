# MIT6.00.1x
My solutions for MIT 6.00.1x course on edX.

**Bear in mind: I have not solved some of the problems, so good luck solving them!**

### L3 Problem 9

In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

Here is a transcript of an example session:
```
Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83
```

Your program should use bisection search. So think carefully what that means. What will the first guess always be? How should you calculate subsequent guesses?

### L4 Problem 5
Write a Python function, `clip(lo, x, hi)` that returns `lo` if `x` is less than `lo`; `hi` if `x` is greater than `hi`; and `x` otherwise. For this problem, you can assume that `lo < hi`.

Don't use any conditional statements for this problem. Instead, use the built in Python functions min and max. You may wish to read the documentation on min and the documentation on max, and play around with these functions a bit in your interpreter, before beginning this problem.

This function takes in three numbers and returns a single number.

### L4 Problem 8

Write a Python function, `fourthPower`, that takes in one number and returns that value raised to the fourth power.

You should use the `square` procedure that you defined in Problem 3 of these lecture exercises (you don't need to redefine `square` in this box; when you call `square`, the tutor will use our definition).

This function takes in one number and returns one number.

### L4 Problem 9

Write a Python function, `odd`, that takes in one number and returns `True` when the number is odd and `False` otherwise.

You should use the `%` (mod) operator, not `if`.

This function takes in one number and returns a boolean.

### L4 Problem 10

Define a function `isVowel(char)` that returns `True` if char is a vowel ('a', 'e', 'i', 'o', or 'u'), and `False` otherwise. You can assume that `char` is a single letter of any case (ie, 'A' and 'a' are both valid).

Do not use the keyword `in`. Your function should take in a single string and return a boolean.

### L4 Problem 11

Define a function `isVowel2(char)` that returns `True` if char is a vowel ('a', 'e', 'i', 'o', or 'u'), and `False` otherwise. You can assume that `char` is a single letter of any case (ie, 'A' and 'a' are both valid).

This function is similar to the previous problem - but this time, do use the keyword `in`. Your function should take in a single string and return a boolean.

### L12 Problem 3

To begin: Download L12_hand.py and read through the file. Be sure to understand what's going on in the file. Make a few instances of the Hand class, and play around with the existing methods.

When you have completed reading through the file, implement the update method.

The \_\_str__ method is this:
```
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        for letter in sorted(self.hand.keys()):
            output += letter * self.hand[letter]
        return output
```

### L12 Problem 5

Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
