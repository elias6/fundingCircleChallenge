#!/usr/bin/env python3

import unittest

from prime_challenge import PrimeFinder, format_number

class TestPrimeFinder(unittest.TestCase):
    def test_prime_finder(self):
        prime_finder = PrimeFinder()
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        for i in range(-1, 21):
            self.assertEqual(prime_finder.is_prime(i),
                             i in primes,
                             "wrong result for is_prime({})".format(i))

    def test_format_number(self):
        self.assertEqual("        ", format_number(1, length=8))
        self.assertEqual("       2", format_number(2, length=8))
        self.assertEqual("   2,345", format_number(2345, length=8))

if __name__ == "__main__":
    unittest.main()
