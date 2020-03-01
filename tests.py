import unittest
import math
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_area(self):
        expected = 25 * math.pi
        self.assertEqual(expected, task.calculate_area(5))


if __name__ == '__main__':
    unittest.main()
