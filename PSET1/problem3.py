subS = ''
print "s = " + s
for x in range(len(s)-1):
    tmpS = s[x]
    for y in range(x+1, len(s)):
        if tmpS[-1] <= s[y]:
            tmpS = tmpS + s[y]
        else:
            break
    if len(tmpS) > len(subS):
        subS = tmpS
print "Longest substring in alphabetical order is: " + subS
