# sum_primes_without_pp.py
import math, sys, time

def isprime(n):
    """Returns True if n is prime and False otherwise"""
    if not isinstance(n, int):
        raise TypeError("argument passed to is_prime is not of 'int' type")
    if n < 2:
        return False
    if n == 2:
        return True
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= max:
        if n % i == 0:
            return False
        i += 1
    return True

def sum_primes(n):
    """Calculates sum of all primes below given integer n"""
    return sum([x for x in xrange(2,n) if isprime(x)])


start_time = time.time()
inputs = (100000, 100100, 100200, 100300, 100400, 100500, 100600, 100700)
for input in inputs:
    print "Sum of primes below", input, "is", sum_primes(input)

print "Time elapsed: ", time.time() - start_time, "s"