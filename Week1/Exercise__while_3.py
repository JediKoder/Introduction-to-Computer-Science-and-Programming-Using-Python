### Exercise WHILE #3

#Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you.
#So, for example, if we define end to be 6, your code should print out the result:
#
# 21 which is 1 + 2 + 3 + 4 + 5 + 6.

# Test
end = 6

total = 0

while end > 0:
    total += end
    end -= 1

print(total)
