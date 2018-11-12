#Prime Number Finder

primes = []
for number in range(2, 100):
    for trial in primes:
        div = number / trial
        if int(div) == div:
            break
    else:
        primes.append(number)

differences = []
for prime1, prime2 in zip(primes, primes[1:]):
    differences.append(prime2 - prime1)
