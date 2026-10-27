"""Mathematical model of a parametric heart curve."""

import math


class HeartModel:
    """Generate points for a heart using a standard parametric equation."""

    def point_at(self, angle):
        """Return one point on the curve for an angle in radians.

        The familiar curve is x = 16 sin(t)^3 and
        y = 13 cos(t) - 5 cos(2t) - 2 cos(3t) - cos(4t).
        The y coordinate is inverted later because screen coordinates grow down.
        """
        x = 16 * math.sin(angle) ** 3
        y = (
            13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle)
        )
        return x, y

    def points_until(self, end_angle, samples=900):
        """Return curve points from zero up to ``end_angle``."""
        count = max(2, int(samples * end_angle / (2 * math.pi)))
        return [self.point_at(end_angle * index / count) for index in range(count + 1)]
