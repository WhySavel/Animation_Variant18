"""Canvas renderer for the animated heart."""

import math


class HeartRenderer:
    """Draw the curve and a subtle glow on a Tkinter canvas."""

    def __init__(self, model):
        """Store the mathematical model."""
        self.model = model

    def draw(self, canvas, width, height, end_angle, scale):
        """Render the visible part of the heart curve."""
        canvas.delete("animation")
        center_x = width / 2
        center_y = height / 2 + 5
        points = self.model.points_until(end_angle)

        if len(points) < 2:
            return

        flat = []
        for x, y in points:
            flat.extend((center_x + x * scale, center_y - y * scale))

        # Multiple wider lines create a simple glow without extra libraries.
        if len(flat) >= 4:
            canvas.create_line(
                *flat, fill="#67294b", width=11, smooth=True,
                capstyle="round", tags="animation"
            )
            canvas.create_line(
                *flat, fill="#c83f70", width=5, smooth=True,
                capstyle="round", tags="animation"
            )
            canvas.create_line(
                *flat, fill="#ff8bad", width=2, smooth=True,
                capstyle="round", tags="animation"
            )

        # A small marker shows the current end of the animated line.
        px, py = points[-1]
        x = center_x + px * scale
        y = center_y - py * scale
        canvas.create_oval(
            x - 4, y - 4, x + 4, y + 4,
            fill="#fff0f5", outline="", tags="animation"
        )

        canvas.create_text(
            18, 18, anchor="nw",
            text=f"Угол: {end_angle:.2f} рад",
            fill="#b8bfd8", font=("Segoe UI", 10),
            tags="animation"
        )
