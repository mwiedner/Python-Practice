limit = 2000000

def primes_sum(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i**2, n + 1, i):
                sieve[j] = False
    return sum(i for i in range(n) if sieve[i])

print(primes_sum(limit))