"""Basic tests for the heart curve model."""

import math
import unittest

from src.models.heart_model import HeartModel


class HeartModelTests(unittest.TestCase):
    """Check important properties of the curve."""

    def setUp(self):
        self.model = HeartModel()

    def test_start_and_end_points_match(self):
        """The full curve should return to its starting point."""
        first = self.model.point_at(0)
        last = self.model.point_at(2 * math.pi)
        self.assertAlmostEqual(first[0], last[0], places=7)
        self.assertAlmostEqual(first[1], last[1], places=7)

    def test_point_is_pair_of_numbers(self):
        """A point contains x and y coordinates."""
        point = self.model.point_at(math.pi / 3)
        self.assertEqual(len(point), 2)
        self.assertTrue(all(isinstance(value, float) for value in point))


if __name__ == "__main__":
    unittest.main()
