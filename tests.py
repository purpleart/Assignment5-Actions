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

    def test_get_first_last_elements(self):
        my_list = [0, 1, 2, 3, 4, 5]
        expected_first, expected_last = 0, 5
        actual_first, actual_last = task.get_first_last_elements(my_list)
        self.assertEqual(expected_first, actual_first)
        self.assertEqual(expected_last, actual_last)


if __name__ == '__main__':
    unittest.main()
