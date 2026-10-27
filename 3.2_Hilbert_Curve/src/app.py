"""Tkinter application for an animated Hilbert curve."""

import tkinter as tk
from tkinter import ttk

from src.models.hilbert_model import HilbertModel
from src.renderers.hilbert_renderer import HilbertRenderer


class HilbertAnimationApp:
    """Manage UI controls and the step-by-step curve animation."""

    def __init__(self):
        """Initialize the window and drawing state."""
        self.root = tk.Tk()
        self.root.title("3.2 — Кривая Гильберта | Вариант 18")
        self.root.geometry("1000x760")
        self.root.minsize(760, 600)
        self.root.configure(bg="#10121d")

        self.model = HilbertModel()
        self.renderer = HilbertRenderer()
        self.order = 4
        self.path = self.model.generate(self.order)
        self.drawn_segments = 0
        self.running = True
        self.speed = 5
        self.color_shift = 0.0

        self._build_ui()
        self._animate()

    def _build_ui(self):
        """Create the canvas and controls."""
        tk.Label(
            self.root,
            text="КРИВАЯ ГИЛЬБЕРТА",
            font=("Segoe UI", 21, "bold"),
            fg="#9ce7ff",
            bg="#10121d",
        ).pack(pady=(14, 2))

        tk.Label(
            self.root,
            text="Рекурсивная кривая, заполняющая пространство • вариант 18",
            font=("Segoe UI", 10),
            fg="#b8bfd8",
            bg="#10121d",
        ).pack(pady=(0, 10))

        self.canvas = tk.Canvas(
            self.root, bg="#10121d", highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True, padx=16, pady=6)

        controls = ttk.Frame(self.root, padding=(16, 8))
        controls.pack(fill="x")

        self.pause_button = ttk.Button(
            controls, text="Пауза", command=self._toggle_pause
        )
        self.pause_button.pack(side="left", padx=(0, 8))
        ttk.Button(controls, text="Заново", command=self._restart).pack(
            side="left", padx=4
        )

        ttk.Label(controls, text="Порядок").pack(side="left", padx=(18, 6))
        self.order_var = tk.IntVar(value=self.order)
        order_box = ttk.Combobox(
            controls, textvariable=self.order_var,
            values=(1, 2, 3, 4, 5, 6), width=4, state="readonly"
        )
        order_box.pack(side="left")
        order_box.bind("<<ComboboxSelected>>", self._change_order)

        ttk.Label(controls, text="Скорость").pack(side="left", padx=(18, 6))
        self.speed_var = tk.IntVar(value=self.speed)
        speed_scale = ttk.Scale(
            controls, from_=1, to=16, variable=self.speed_var,
            command=self._change_speed, length=130
        )
        speed_scale.pack(side="left")

        ttk.Label(
            controls, text="Пробел — пауза   •   R — заново"
        ).pack(side="right", padx=8)

        self.root.bind("<space>", lambda _event: self._toggle_pause())
        self.root.bind("r", lambda _event: self._restart())
        self.root.bind("R", lambda _event: self._restart())

    def _change_order(self, _event=None):
        """Regenerate the curve after changing its recursion order."""
        self.order = int(self.order_var.get())
        self.path = self.model.generate(self.order)
        self.drawn_segments = 0
        self.color_shift = 0.0
        self.canvas.delete("curve")

    def _change_speed(self, value):
        """Read the speed slider value."""
        self.speed = max(1, int(float(value)))

    def _toggle_pause(self):
        """Pause or resume the animation."""
        self.running = not self.running
        self.pause_button.configure(
            text="Продолжить" if not self.running else "Пауза"
        )

    def _restart(self):
        """Clear the current curve and start from the first segment."""
        self.drawn_segments = 0
        self.color_shift = 0.0
        self.canvas.delete("curve")

    def _animate(self):
        """Draw several additional segments and schedule the next frame."""
        if self.running and self.drawn_segments < len(self.path) - 1:
            self.drawn_segments = min(
                len(self.path) - 1, self.drawn_segments + self.speed
            )
            self.color_shift += 0.012
            self.renderer.draw(
                self.canvas,
                self.path[: self.drawn_segments + 1],
                self.order,
                self.color_shift,
                self.canvas.winfo_width(),
                self.canvas.winfo_height(),
            )
        self.root.after(30, self._animate)

    def run(self):
        """Start Tkinter's main event loop."""
        self.root.mainloop()
