import unittest

from src.max_number import max_number, max_number_index


class TestMaxFunction(unittest.TestCase):
    def test_empty(self):
        with self.assertRaises(ValueError):
            max_number([])

    def test_single_positive(self):
        self.assertEqual(max_number([5]), 5)

    def test_multiple_positives(self):
        self.assertEqual(max_number([1, 2, 3]), 3)

    def test_single_negative(self):
        self.assertEqual(max_number([-5]), -5)

    def test_multiple_negatives(self):
        self.assertEqual(max_number([-1, -2, -3]), -1)

    def test_mixed_values(self):
        self.assertEqual(max_number([-1, 0, 1]), 1)

    def test_max_with_zero(self):
        self.assertEqual(max_number([0, -10, 10]), 10)

    def test_identical_values(self):
        self.assertEqual(max_number([3, 3, 3]), 3)

    def test_large_values(self):
        self.assertEqual(max_number([1000000000, 500000000, 1000000001]), 1000000001)

    def test_small_values(self):
        self.assertEqual(max_number([1e-12, 2e-12, 3e-12]), 3e-12)

    def test_with_infinity(self):
        self.assertEqual(max_number([float('inf'), 1, 2]), float('inf'))
        self.assertEqual(max_number([-float('inf'), -1, -2]), -1)

    def test_single_item_list(self):
        self.assertEqual(max_number([5]), 5)

    def test_multiple_items_list(self):
        self.assertEqual(max_number([1, 2, 3]), 3)

    def test_nested_lists(self):
        self.assertEqual(max_number([[1, 2], [3, 4], [5, 6]]), [5, 6])
        self.assertEqual(max_number([[1, 2, 3], [1, 2]]), [1, 2, 3])

    def test_strings(self):
        self.assertEqual(max_number(['a', 'b', 'c']), 'c')
        self.assertEqual(max_number(['abc', 'def', 'ghi']), 'ghi')


def max_index(list_of_values):
    if not list_of_values:
        raise ValueError("The input list cannot be empty.")
    max_val = list_of_values[0]
    max_idx = 0

    for idx, val in enumerate(list_of_values):
        if val > max_val:
            max_val = val
            max_idx = idx

    return max_idx


class TestMaxIndexFunction(unittest.TestCase):
    def test_single_positive(self):
        self.assertEqual(max_number_index([5]), 0)

    def test_multiple_positives(self):
        self.assertEqual(max_number_index([1, 2, 3]), 2)

    def test_single_negative(self):
        self.assertEqual(max_number_index([-5]), 0)

    def test_multiple_negatives(self):
        self.assertEqual(max_number_index([-1, -2, -3]), 0)

    def test_mixed_values(self):
        self.assertEqual(max_number_index([-1, 0, 1]), 2)

    def test_max_with_zero(self):
        self.assertEqual(max_number_index([0, -10, 10]), 2)

    def test_identical_values(self):
        self.assertEqual(max_number_index([3, 3, 3]), 0)

    def test_large_values(self):
        self.assertEqual(max_number_index([1000000000, 500000000, 1000000001]), 2)

    def test_small_values(self):
        self.assertEqual(max_number_index([1e-12, 2e-12, 3e-12]), 2)

    def test_with_infinity(self):
        self.assertEqual(max_number_index([float('inf'), 1, 2]), 0)
        self.assertEqual(max_number_index([-float('inf'), -1, -2]), 1)

    def test_single_item_list(self):
        self.assertEqual(max_number_index([5]), 0)

    def test_multiple_items_list(self):
        self.assertEqual(max_number_index([1, 2, 3]), 2)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            max_number_index([])


if __name__ == '__main__':
    unittest.main()

