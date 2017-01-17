import unittest
import prime_no_function

class PrimeNumberTest(unittest.TestCase):
    def setUp(self):
        self.negative= prime_no_function.number(-78)
        self.string = prime_no_function.number("Andela")
        self.prime_no_array = prime_no_function.array_of_prime_integers(77)

    def test_if_list_is_empty(self):
        self.assertEqual(prime_no_function.array_of_prime_integers(0), [])

    def test_if_input_is_negative(self):
        for x in range(-1, self.negative, -1):
            self.assertFalse(prime_no_function.prime(x))

    def test_if_array_of_prime_number_has_non_prime_numbers(self):
        # zero signifies
        for i in self.prime_no_array:
            self.assertTrue(prime_no_function.prime(i))

    def test_that_zero_is_not_a_prime_number(self):
        self.assertFalse(prime_no_function.prime(0))

    def test_if_known_prime_returns_true(self):
        self.assertTrue(prime_no_function.prime(13))
    