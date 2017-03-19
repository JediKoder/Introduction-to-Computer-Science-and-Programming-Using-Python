# Problem #3:

#Assume s is a string of lower case characters.
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
#For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

#Longest substring in alphabetical order is: abc

# Test

s = 'azcbobobegghakl'
#s = 'abcbcd'
#s = 'abcdefghijklmnopqrstuvwxyz'
#s = 'zyxwvutsrqponmlkjihgfedcba'

#######################
longest = ''
temp_string = s[0]

for idx in range(len(s)-1):
    if s[idx+1] >= s[idx]:
        temp_string += s[idx+1]
        print(temp_string)
    else:
        if len(temp_string) > len(longest):
            longest = temp_string
        temp_string = s[idx+1]

    if len(temp_string) > len(longest):
            longest = temp_string

print("Longest substring in alphabetical order is: ", longest)
