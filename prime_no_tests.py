import unittest
import prime_no_function

class PrimeNumberTest(unittest.TestCase):
    def setUp(self):
        self.nonPositive= prime_numbers.number(-78)
        self.string = prime_numbers.number("Andela")

    def test_if_list_is_empty(self):
        self.assertEqual(prime_numbers.array_of_prime_integers(0), [])

    def test_that_zero_is_not_a_prime_number(self):
        self.assertFalse(prime_numbers.prime(0))

