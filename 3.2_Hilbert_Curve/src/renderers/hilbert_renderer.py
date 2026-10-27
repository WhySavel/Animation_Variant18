"""Canvas drawing and color handling for the Hilbert curve."""

import colorsys


class HilbertRenderer:
    """Render a Hilbert path with a smooth color transition."""

    def draw(self, canvas, points, order, color_shift, width, height):
        """Draw all supplied points, coloring segments by their position."""
        canvas.delete("curve")
        if len(points) < 2:
            return

        margin = 34
        side = max(20, min(width, height) - 2 * margin)
        # Keep the drawing centered and preserve the square proportions.
        left = (width - side) / 2
        top = (height - side) / 2

        for index in range(1, len(points)):
            x1, y1 = points[index - 1]
            x2, y2 = points[index]
            sx1 = left + x1 * side
            sy1 = top + y1 * side
            sx2 = left + x2 * side
            sy2 = top + y2 * side

            hue = (index / max(1, len(points) - 1) + color_shift) % 1.0
            red, green, blue = colorsys.hsv_to_rgb(hue, 0.72, 1.0)
            color = f"#{int(red * 255):02x}{int(green * 255):02x}{int(blue * 255):02x}"
            canvas.create_line(
                sx1, sy1, sx2, sy2,
                fill=color, width=max(1, 4 - order // 2),
                capstyle="round", tags="curve"
            )

        canvas.create_text(
            18, 18, anchor="nw",
            text=f"Порядок: {order}   Точек: {len(points)}",
            fill="#b8bfd8", font=("Segoe UI", 10), tags="curve"
        )
