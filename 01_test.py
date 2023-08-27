import unittest
from geo_module import zipcode_validation, validation_digit


class TestSum(unittest.TestCase):

    def test_zipCode_numeric(self):
        self.assertIsNotNone(zipcode_validation(
            "5521"))
        self.assertIsNotNone(validation_digit(
            "5521"))

    def test_zipCode_abcd(self):
        self.assertIsNotNone(zipcode_validation(
            "abc"))
        self.assertIsNotNone(validation_digit(
            "abc"))

    def test_error_abc(self):
        text_error = "Please enter a valid numeric zip code"
        self.assertEqual(validation_digit(
            "abc"), text_error)
        self.assertEqual(validation_digit("aaabbb"), text_error)


if __name__ == '__main__':
    unittest.main()
