import unittest
from project8 import ConvertBin2Hex

class BinaryToHexConverterTest(unittest.TestCase):

    def setUp(self):
        # Create an instance of the class to test
        self.single = ConvertBin2Hex("1001")
        self.letter = ConvertBin2Hex("1111")
        self.string = ConvertBin2Hex("1010 1111")

    def test_single_digit(self):
        # Test a single hex value between 0 and 9
        expected = '9'
        result = self.single.hexValue
        self.assertEqual(result, expected, "Conversion failed for a single digit.")

    def test_single_letter(self):
        # Test a single hex value between A and F
        expected = 'F'
        result = self.letter.hexValue
        self.assertEqual(result, expected, "Conversion failed for a single letter.")

    def test_two_hex_values(self):
        # Test a case with two hex values
        expected = 'AF'
        result = self.string.hexValue
        self.assertEqual(result, expected, "Conversion failed for two hex values.")

    def test_invalid_input(self):
        # Test an invalid input case
        invalid_input = "Invalid Input"
        with self.assertRaises(ValueError):
            # Use assertRaises to check if the expected exception is raised
            ConvertBin2Hex(invalid_input)

if __name__ == '__main__':
    unittest.main()
