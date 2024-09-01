import tkinter as tk, winaccent, threading
from tkinter import ttk

window = tk.Tk()
window.title("Accent color palette")
window.resizable(False, False)
window.configure(padx = 8, pady = 8)

style = ttk.Style()
style.configure("TButton", font = 11)

def add_item(color, text):
    color_item = tk.Frame(window, padx = 8, pady = 0)
    color_item.pack(pady = 2, anchor = "w")

    tk.Frame(color_item, width = 20, height = 20, bg = color, highlightthickness = 1, highlightbackground = "#000000").pack(side = "left")
    tk.Label(color_item, text = f"{text}:          {color}", font = ("Default", 11)).pack(side = "left", padx = (8, 0))

def update_accent_colors():
    winaccent.update_accent_colors()
    for widget in window.winfo_children(): widget.destroy()

    add_item(winaccent.accent_light_3, "accent_light_3")
    add_item(winaccent.accent_light_2, "accent_light_2")
    add_item(winaccent.accent_light_1, "accent_light_1")
    add_item(winaccent.accent_normal, "accent_normal")
    add_item(winaccent.accent_dark_1, "accent_dark_1")
    add_item(winaccent.accent_dark_2, "accent_dark_2")
    add_item(winaccent.accent_dark_3, "accent_dark_3")

update_accent_colors()

thread = threading.Thread(target = lambda: winaccent.on_accent_changed_listener(update_accent_colors), daemon = True)
thread.start()

window.mainloop()