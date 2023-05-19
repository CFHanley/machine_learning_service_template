import unittest
from main import add_two_numbers_together


class MyTestCase(unittest.TestCase):
    def test_add_two_numbers_together_pass(self):
        value = add_two_numbers_together(1, 2)

        self.assertEqual(value, 3)

    def test_add_two_numbers_together_fail(self):
        value = add_two_numbers_together(1, 2)

        self.assertNotEqual(value, 10)
