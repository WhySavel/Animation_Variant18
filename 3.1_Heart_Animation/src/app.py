"""Tkinter interface and animation loop for the heart curve."""

import math
import tkinter as tk
from tkinter import ttk

from src.models.heart_model import HeartModel
from src.renderers.heart_renderer import HeartRenderer


class HeartAnimationApp:
    """Manage the window, controls, and animated drawing of a heart."""

    def __init__(self):
        """Create widgets and initialize the animation state."""
        self.root = tk.Tk()
        self.root.title("3.1 — Сердце | Вариант 18")
        self.root.geometry("960x720")
        self.root.minsize(760, 580)
        self.root.configure(bg="#10121d")

        self.model = HeartModel()
        self.renderer = HeartRenderer(self.model)
        self.running = True
        self.draw_angle = 0.0
        self.angle_step = 0.075
        self.scale = 13.0

        self._build_ui()
        self._animate()

    def _build_ui(self):
        """Build the title, canvas, and control panel."""
        title = tk.Label(
            self.root,
            text="СЕРДЦЕ",
            font=("Segoe UI", 22, "bold"),
            fg="#ff6b91",
            bg="#10121d",
        )
        title.pack(pady=(14, 2))

        subtitle = tk.Label(
            self.root,
            text="Полярная параметрическая кривая • вариант 18",
            font=("Segoe UI", 10),
            fg="#b8bfd8",
            bg="#10121d",
        )
        subtitle.pack(pady=(0, 10))

        self.canvas = tk.Canvas(
            self.root,
            bg="#10121d",
            highlightthickness=0,
        )
        self.canvas.pack(fill="both", expand=True, padx=18, pady=6)

        controls = ttk.Frame(self.root, padding=(18, 8))
        controls.pack(fill="x")

        self.pause_button = ttk.Button(
            controls, text="Пауза", command=self._toggle_pause
        )
        self.pause_button.pack(side="left", padx=(0, 8))

        ttk.Button(
            controls, text="Заново", command=self._reset
        ).pack(side="left", padx=4)

        ttk.Label(controls, text="Скорость").pack(side="left", padx=(22, 8))
        self.speed = tk.DoubleVar(value=0.075)
        speed_scale = ttk.Scale(
            controls,
            from_=0.02,
            to=0.18,
            variable=self.speed,
            command=self._change_speed,
            length=180,
        )
        speed_scale.pack(side="left")

        ttk.Label(
            controls,
            text="Пробел — пауза   •   R — сначала",
        ).pack(side="right", padx=8)

        self.root.bind("<space>", lambda _event: self._toggle_pause())
        self.root.bind("r", lambda _event: self._reset())
        self.root.bind("R", lambda _event: self._reset())
        self.root.bind("<Configure>", self._on_resize)

    def _on_resize(self, event):
        """Adjust the scale when the main window is resized."""
        if event.widget is self.root:
            self.scale = max(8.0, min(16.0, min(event.width, event.height) / 48))

    def _change_speed(self, value):
        """Update the angular increment from the speed slider."""
        self.angle_step = float(value)

    def _toggle_pause(self):
        """Pause or resume the drawing loop."""
        self.running = not self.running
        self.pause_button.configure(text="Продолжить" if not self.running else "Пауза")

    def _reset(self):
        """Clear the canvas and restart the curve animation."""
        self.draw_angle = 0.0
        self.canvas.delete("all")

    def _animate(self):
        """Draw another segment and schedule the next frame."""
        width = max(1, self.canvas.winfo_width())
        height = max(1, self.canvas.winfo_height())
        if self.running:
            self.draw_angle = min(self.draw_angle + self.angle_step, 2 * math.pi)
            self.renderer.draw(
                self.canvas,
                width,
                height,
                self.draw_angle,
                self.scale,
            )
            if self.draw_angle >= 2 * math.pi:
                self.draw_angle = 0.0
                self.canvas.after(900, self._animate)
                return
        self.root.after(16, self._animate)

    def run(self):
        """Start Tkinter's main event loop."""
        self.root.mainloop()
