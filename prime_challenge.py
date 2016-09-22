#!/usr/bin/env python3

from argparse import ArgumentParser
from itertools import count, islice, takewhile
from math import ceil, sqrt

class PrimeFinder:
    def __init__(self):
        self._sieve = []
        self._sieve_set = set()
        self._sieve_max = 1

    def fill_sieve(self, limit):
        for i in range(self._sieve_max + 1, limit + 1):
            sieve_iter = takewhile(lambda y: y <= ceil(sqrt(i)), self._sieve)
            if all(i % j != 0 for j in sieve_iter):
                self._sieve.append(i)
                self._sieve_set.add(i)
        self._sieve_max = limit

    def is_prime(self, x):
        if x <= 1:
            return False
        if x <= self._sieve_max:
            return x in self._sieve_set
        self.fill_sieve(ceil(sqrt(x)))
        sieve_iter = takewhile(lambda y: y**2 <= x, self._sieve)
        return all(x % y != 0 for y in sieve_iter)

    def first_primes(self, n):
        return islice((i for i in count(start=1) if self.is_prime(i)), n)


def format_number(x, length):
    if x == 1:
        return " " * length
    else:
        return ("{:" + str(length) + ",}").format(x)

if __name__ == "__main__":
    parser = ArgumentParser(
        description="Print a multiplication table of the first n prime numbers.")
    parser.add_argument("n", type=int, default=10, nargs="?",
        help="Number of primes to use for the table")
    args = parser.parse_args()

    primes = list(PrimeFinder().first_primes(args.n))
    product_length = len("{:,}".format(max(primes) ** 2))

    for x in [1] + primes:
        print("  ".join(format_number(x * y, product_length) for y in [1] + primes))
