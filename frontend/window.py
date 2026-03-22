import tkinter as tk

BAR_HEIGHT = 48
BAR_COLOR = "#1e1e1e"
TEXT_COLOR = "#ffffff"
ACCENT_COLOR = "#4ade80"  # green for active gesture
ERROR_COLOR = "#f87171"


class App:
    def __init__(self, root: tk.Tk, state: dict):
        self.root = root
        self.state = state

        # --- Window chrome ---
        self.root.overrideredirect(True)       # removes title bar / borders
        self.root.attributes("-topmost", True) # always on top
        self.root.attributes("-alpha", 0.92)   # slight transparency
        self.root.configure(bg=BAR_COLOR)

        # Pin to top-center of screen
        sw = self.root.winfo_screenwidth()
        BAR_WIDTH = 480
        x = (sw - BAR_WIDTH) // 2
        self.root.geometry(f"{BAR_WIDTH}x{BAR_HEIGHT}+{x}+0")

        self._build_ui()
        self._poll()

    def _build_ui(self):
        frame = tk.Frame(self.root, bg=BAR_COLOR)
        frame.pack(fill="both", expand=True, padx=12)

        # Dot indicator
        self.dot = tk.Label(frame, text="●", bg=BAR_COLOR, fg=ACCENT_COLOR, font=("Helvetica", 10))
        self.dot.pack(side="left", padx=(0, 8))

        # Gesture label
        tk.Label(frame, text="Gesture:", bg=BAR_COLOR, fg="#888888",
                 font=("Helvetica", 11)).pack(side="left")
        self.gesture_var = tk.StringVar(value="—")
        tk.Label(frame, textvariable=self.gesture_var, bg=BAR_COLOR, fg=TEXT_COLOR,
                 font=("Helvetica", 11, "bold"), width=14, anchor="w").pack(side="left", padx=(4, 0))

        # Close button on the right
        close_btn = tk.Label(frame, text="✕", bg=BAR_COLOR, fg="#666666",
                    font=("Helvetica", 11), cursor="hand2")
        close_btn.pack(side="right")
        close_btn.bind("<Button-1>", lambda e: self._close())

        # Allow dragging the bar
        frame.bind("<ButtonPress-1>", self._drag_start)
        frame.bind("<B1-Motion>", self._drag_motion)

    def _poll(self):
        if not self.state.get("cam"):
            self.gesture_var.set("Camera not found")
            self.dot.config(fg=ERROR_COLOR)
            self.root.after(50, self._poll)
            return
        gesture = self.state.get("gesture")
        self.gesture_var.set(gesture or "—")
        self.dot.config(fg=ACCENT_COLOR if gesture else "#444444")
        self.root.after(50, self._poll)

    def _drag_start(self, event):
        self._drag_x = event.x_root - self.root.winfo_x()
        self._drag_y = event.y_root - self.root.winfo_y()

    def _drag_motion(self, event):
        x = event.x_root - self._drag_x
        y = event.y_root - self._drag_y
        self.root.geometry(f"+{x}+{y}")

    def _close(self):
        self.state["running"] = False
        self.root.destroy()