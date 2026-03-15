import sys, os, threading, tkinter as tk
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.main import main as backend_main  # aliased to avoid collision
from frontend.window import App

def main():
    state = {"gesture": None, "running": True}

    threading.Thread(target=backend_main, args=(state,), daemon=True).start()

    root = tk.Tk()
    App(root, state)
    root.protocol("WM_DELETE_WINDOW", lambda: (state.update({"running": False}), root.destroy()))
    root.mainloop()

if __name__ == "__main__":
    main()