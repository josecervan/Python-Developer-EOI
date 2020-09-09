import power_of_four
import unittest


class Test(unittest.TestCase):

    def test_isPowerOfFour(self):
        self.assertTrue(power_of_four.isPowerOfFour(1))
        self.assertTrue(power_of_four.isPowerOfFour(4))
        self.assertTrue(power_of_four.isPowerOfFour(16))
        self.assertTrue(power_of_four.isPowerOfFour(64))
        self.assertTrue(power_of_four.isPowerOfFour(256))

        self.assertFalse(power_of_four.isPowerOfFour(4.4))
        self.assertFalse(power_of_four.isPowerOfFour(15))
        self.assertFalse(power_of_four.isPowerOfFour(297))
        self.assertFalse(power_of_four.isPowerOfFour(1004))
        self.assertFalse(power_of_four.isPowerOfFour(159))
