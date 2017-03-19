# Problem #2:

#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s.
#For example, if s = 'azcbobobegghakl', then your program should print:

#Number of times bob occurs is: 2

# Test

s = 'azcbobobegghakl'

count = 0
idx = 0
for char in s:
    if s[idx:idx+3] == 'bob':
        count += 1
    idx += 1

print("Number of times bob occurs is: " + str(count))
