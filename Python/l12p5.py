def genPrimes():
    generatedPrimes = []
    if len(generatedPrimes) == 0:
        yield 2
        generatedPrimes.append(2)
    x = 2
    while True:
        isPrime = True
        for p in generatedPrimes:
            if (x % p) == 0:
                isPrime = False
        if isPrime:
            yield x
            generatedPrimes.append(x)
        x += 1
