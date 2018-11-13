#Prime Number Finder

PRIME_LIST_LENGTH = 100

def get_primes(amount):
    primes = []
    for number in range(2, amount):
        for trial in primes:
            div = number / trial
            if int(div) == div:
                break
        else:
            primes.append(number)
    return primes

primes = get_primes(PRIME_LIST_LENGTH)

differences = [prime2 - prime1 for prime1, prime2 in zip(primes, primes[1:])]
