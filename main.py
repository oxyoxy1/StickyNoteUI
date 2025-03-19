import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import os

NOTES_DIR = "Notes"
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

class StickyNote:
    def __init__(self, root, filename):
        self.root = root
        self.filename = filename
        self.is_pinned = False

        # Set window title
        self.root.title(os.path.basename(filename))

        # Set sticky note look
        self.root.geometry("400x300")
        self.root.resizable(True, True)  # Make the sticky note resizable

        # Make window look like a sticky note (yellow background, no border)
        self.root.configure(bg="#f7f2a3")  # Yellow sticky note color
        self.root.attributes("-topmost", True)  # Keep the sticky note on top

        # Make the window draggable
        self._drag_data = {"x": 0, "y": 0}
        self.root.bind("<ButtonPress-1>", self._on_drag_start)
        self.root.bind("<B1-Motion>", self._on_drag_motion)

        # Main layout using grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)  # Text area expands
        self.root.rowconfigure(1, weight=0)  # Buttons stay fixed

        # Text area (casual font to mimic handwritten text)
        self.text_area = tk.Text(self.root, wrap="word", font=("Comic Sans MS", 12), bg="#f7f2a3", bd=0, highlightthickness=0)
        self.text_area.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Button frame (fixed height)
        self.button_frame = tk.Frame(self.root, bg="#f7f2a3")
        self.button_frame.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_note, bg="#d3d3d3")  # Light gray background
        self.save_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        self.save_as_button = tk.Button(self.button_frame, text="Save As", command=self.save_as, bg="#d3d3d3")  # Light gray background
        self.save_as_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        self.pin_button = tk.Button(self.button_frame, text="Pin", command=self.toggle_pin, bg="#d3d3d3")  # Light gray background
        self.pin_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        # Load note if it exists
        if os.path.exists(self.filename):
            self.load_note()

    def load_note(self):
        """Loads the note content if the file exists."""
        with open(self.filename, "r") as file:
            self.text_area.insert(tk.END, file.read())

    def save_note(self):
        """Saves the note to the assigned filename."""
        with open(self.filename, "w") as file:
            file.write(self.text_area.get("1.0", tk.END).strip())

    def save_as(self):
        """Saves the note with a new name."""
        new_filename = filedialog.asksaveasfilename(
            defaultextension=".txt", initialdir=NOTES_DIR, filetypes=[("Text Files", "*.txt")]
        )
        if new_filename:
            self.filename = new_filename
            self.root.title(os.path.basename(new_filename))
            self.save_note()

    def toggle_pin(self):
        """Toggles the pin state (always on top)."""
        self.is_pinned = not self.is_pinned
        self.root.attributes("-topmost", self.is_pinned)

    def _on_drag_start(self, event):
        """Records the initial position for dragging."""
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def _on_drag_motion(self, event):
        """Moves the window while dragging."""
        deltax = event.x - self._drag_data["x"]
        deltay = event.y - self._drag_data["y"]
        new_x = self.root.winfo_x() + deltax
        new_y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{new_x}+{new_y}")  # Move the window

class StickyNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sticky Notes UI - oxy")  # Title for main menu
        self.root.geometry("300x200")
        
        # Set the application icon (replace with your icon path)
        self.root.iconbitmap("icon.ico")

        # Make the main app window look like a sticky note launcher (no color changes)
        tk.Button(root, text="New Note", command=self.create_note, bg="#d3d3d3").pack(fill=tk.X, pady=5)  # Light gray background
        tk.Button(root, text="Open Note", command=self.open_note, bg="#d3d3d3").pack(fill=tk.X, pady=5)  # Light gray background
        tk.Button(root, text="Quit", command=root.quit, bg="#d3d3d3").pack(fill=tk.X, pady=5)  # Light gray background

    def create_note(self):
        """Creates a new sticky note with a user-defined title."""        
        note_name = simpledialog.askstring("New Note", "Enter the note title:")
        if note_name:
            filename = os.path.join(NOTES_DIR, f"{note_name}.txt")
            open_note = tk.Toplevel(self.root)
            StickyNote(open_note, filename)

    def open_note(self):
        """Opens an existing sticky note.""" 
        filename = filedialog.askopenfilename(initialdir=NOTES_DIR, filetypes=[("Text Files", "*.txt")])
        if filename:
            open_note = tk.Toplevel(self.root)
            StickyNote(open_note, filename)

if __name__ == "__main__":
    root = tk.Tk()
    app = StickyNoteApp(root)
    root.mainloop()
