import unittest
import SampleApplication

class CalculatorTests(unittest.TestCase):
    """
    A test class for the Calculator functions.
    """

    def test_addition(self):
        """
        Test the add_numbers function.
        :return:
        """
        self.assertEqual(SampleApplication.add_numbers(2, 3), 5)
        self.assertEqual(SampleApplication.add_numbers(-1, 1), 0)
        print("test addition pass!")

    def test_multiplication(self):
        """
        Test the multiply_numbers function.
        :return:
        """
        self.assertEqual(SampleApplication.multiply_numbers(2, 3), 6)
        self.assertEqual(SampleApplication.multiply_numbers(0, 5), 0)
        print("test multiplication pass!")