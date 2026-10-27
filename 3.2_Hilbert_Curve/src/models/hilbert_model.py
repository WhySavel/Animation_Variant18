"""Recursive generator for the Hilbert space-filling curve."""


class HilbertModel:
    """Generate normalized points of a Hilbert curve using recursion."""

    def generate(self, order):
        """Return points for the requested recursion order.

        The recursive routine builds four smaller, rotated copies. Each step
        replaces a square-like path by a more detailed path inside that square.
        """
        order = max(1, min(6, int(order)))
        points = []

        def visit(level, x0, y0, xi, xj, yi, yj):
            """Append points for one oriented square."""
            if level <= 0:
                x = x0 + (xi + yi) / 2
                y = y0 + (xj + yj) / 2
                points.append((x, y))
                return

            visit(level - 1, x0, y0, yi / 2, yj / 2, xi / 2, xj / 2)
            visit(
                level - 1,
                x0 + xi / 2,
                y0 + xj / 2,
                xi / 2,
                xj / 2,
                yi / 2,
                yj / 2,
            )
            visit(
                level - 1,
                x0 + xi / 2 + yi / 2,
                y0 + xj / 2 + yj / 2,
                xi / 2,
                xj / 2,
                yi / 2,
                yj / 2,
            )
            visit(
                level - 1,
                x0 + xi / 2 + yi,
                y0 + xj / 2 + yj,
                -yi / 2,
                -yj / 2,
                -xi / 2,
                -xj / 2,
            )

        visit(order, 0, 0, 1, 0, 0, 1)
        return points
