import unittest
import prime_no_function

class PrimeNumberTest(unittest.TestCase):
    def test_if_list_is_empty(self):
        self.assertEqual(prime_numbers.return_list(0), [])