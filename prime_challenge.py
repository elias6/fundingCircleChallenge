#!/usr/bin/env python3

from itertools import count, islice, takewhile
from math import ceil, sqrt

class PrimeFinder:
    def __init__(self):
        self._sieve = []
        self._sieve_set = set()
        self._sieve_max = 1

    def is_prime(self, x):
        if x <= 1:
            return False
        if x <= self._sieve_max:
            return x in self._sieve_set
        new_max = ceil(sqrt(x))
        for i in range(self._sieve_max + 1, new_max + 1):
            sieve_iter = takewhile(lambda y: y <= ceil(sqrt(i)), self._sieve)
            if all(i % j != 0 for j in sieve_iter):
                self._sieve.append(i)
                self._sieve_set.add(i)
        self._sieve_max = new_max
        sieve_iter = takewhile(lambda y: y < x, self._sieve)
        return all(x % y != 0 for y in sieve_iter)

    def first_primes(self, n):
        return islice((i for i in count(start=1) if self.is_prime(i)), n)


def format_number(x, length):
    if x == 1:
        return " " * length
    else:
        return ("{:" + str(length) + ",}").format(x)

primes = list(PrimeFinder().first_primes(10))
product_length = len("{:,}".format(max(primes) ** 2))

for x in [1] + primes:
    print("  ".join(format_number(x * y, product_length) for y in [1] + primes))
