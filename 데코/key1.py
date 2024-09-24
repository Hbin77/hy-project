import tkinter as tk
from tkinter import messagebox
import keyboard
import json
import os

class ShortcutApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shortcut Setting App")

        self.shortcuts = {}
        self.load_shortcuts()

        self.label = tk.Label(root, text="Press a key combination:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Shortcut", command=self.save_shortcut)
        self.save_button.pack(pady=5)

        self.list_button = tk.Button(root, text="Show Shortcuts", command=self.show_shortcuts)
        self.list_button.pack(pady=5)

        self.root.bind('<Key>', self.record_key)

    def record_key(self, event):
        key_combination = keyboard.get_hotkey_name()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, key_combination)

    def save_shortcut(self):
        shortcut = self.entry.get()
        if shortcut:
            action = "Sample Action"  # Here you can define the action for the shortcut
            self.shortcuts[shortcut] = action
            self.save_shortcuts()
            messagebox.showinfo("Shortcut Saved", f"Shortcut '{shortcut}' saved for action '{action}'")
        else:
            messagebox.showwarning("No Shortcut", "Please enter a shortcut.")

    def show_shortcuts(self):
        shortcuts_str = "\n".join([f"{key}: {action}" for key, action in self.shortcuts.items()])
        messagebox.showinfo("Shortcuts", shortcuts_str if shortcuts_str else "No shortcuts set.")

    def save_shortcuts(self):
        with open("shortcuts.json", "w") as file:
            json.dump(self.shortcuts, file)

    def load_shortcuts(self):
        if os.path.exists("shortcuts.json"):
            with open("shortcuts.json", "r") as file:
                self.shortcuts = json.load(file)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShortcutApp(root)
    root.mainloop()