#!/usr/bin/env python3

import unittest

from prime_challenge import PrimeFinder, format_number

class TestPrimeFinder(unittest.TestCase):
    def test_prime_finder(self):
        prime_finder = PrimeFinder()
        self.assertTrue(prime_finder.is_prime(2))
        self.assertTrue(prime_finder.is_prime(3))
        self.assertTrue(prime_finder.is_prime(5))
        self.assertTrue(prime_finder.is_prime(7))

        self.assertFalse(prime_finder.is_prime(0))
        self.assertFalse(prime_finder.is_prime(1))
        self.assertFalse(prime_finder.is_prime(4))
        self.assertFalse(prime_finder.is_prime(6))
        self.assertFalse(prime_finder.is_prime(8))
        self.assertFalse(prime_finder.is_prime(9))
        self.assertFalse(prime_finder.is_prime(10))

    def test_format_number(self):
        self.assertEqual("        ", format_number(1, length=8))
        self.assertEqual("       2", format_number(2, length=8))
        self.assertEqual("   2,345", format_number(2345, length=8))

if __name__ == "__main__":
    unittest.main()
