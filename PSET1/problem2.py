numberOfBobs = 0
for pos in range(len(s)-2):
    if s[pos:pos+3] == 'bob':
        numberOfBobs += 1
print "Number of times bob occurs: %i" % numberOfBobs
