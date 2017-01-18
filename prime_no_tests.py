import unittest
import prime_no_function

class PrimeNumberTest(unittest.TestCase):
    def setUp(self):
        self.negative= prime_no_function.number(-78)
        self.string = prime_no_function.number("Andela")
        self.prime_no_array = prime_no_function.array_of_prime_integers([7, 7])

    def test_if_list_is_empty(self):
        self.assertEqual(prime_no_function.array_of_prime_integers([]), [])

    def test_if_input_is_negative(self):
        for x in range(-1, self.negative, -1):
            self.assertFalse(prime_no_function.prime(x))

    def test_if_array_of_prime_number_has_prime_numbers(self):
        for i in self.prime_no_array:
            self.assertTrue(prime_no_function.prime(i))

    def test_that_zero_is_not_a_prime_number(self):
        self.assertFalse(prime_no_function.prime(0))

    def test_if_known_prime_returns_true(self):
        self.assertTrue(prime_no_function.prime(13))

    def test_if_input_is_string(self):
        self.assertEqual("invalid format", self.string)

    def test_if_float_is_not_prime(self):
        self.assertEqual("invalid format", prime_no_function.number(3.12))

    def test_if_returns_number_0f_prime_in_array(self):
        self.assertEqual(2, len(self.prime_no_array))

    def test_if_array_only_has_prime_numbers(self):
        self.assertTrue(prime_no_function.array_of_prime_integers([3, 2, 7, 5]))

    def test_if_array_has_non_prime_numbers(self):
        self.assertFalse(prime_no_function.array_of_prime_integers([2, 4, 7, 8]))
if __name__ == "__main__":
    unittest.main()