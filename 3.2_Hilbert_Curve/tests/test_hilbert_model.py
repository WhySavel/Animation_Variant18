"""Basic tests for the Hilbert curve point generator."""

import unittest

from src.models.hilbert_model import HilbertModel


class HilbertModelTests(unittest.TestCase):
    """Check point counts and normalized coordinates."""

    def setUp(self):
        self.model = HilbertModel()

    def test_point_count_grows_by_order(self):
        """An order-n curve contains 4**n points."""
        for order in range(1, 5):
            self.assertEqual(len(self.model.generate(order)), 4 ** order)

    def test_points_are_normalized(self):
        """All generated coordinates should fit inside the unit square."""
        for x, y in self.model.generate(4):
            self.assertGreaterEqual(x, 0)
            self.assertGreaterEqual(y, 0)
            self.assertLessEqual(x, 1)
            self.assertLessEqual(y, 1)


if __name__ == "__main__":
    unittest.main()
