import tkinter as tk, winaccent
from tkinter import ttk

window = tk.Tk()
window.title("winaccent demo program")
window.resizable(False, False)
window.configure(padx = 8, pady = 4)

style = ttk.Style()
style.configure("TButton", font = 11)

def add_item(color, text):
    color_item = tk.Frame(window, padx = 10, pady = 8)
    color_item.pack(pady = 4, anchor = "w")

    tk.Frame(color_item, width = 30, height = 30, bg = color, highlightthickness = 1, highlightbackground = "#000000").pack(side = "left")
    tk.Label(color_item, text = f"{text}: {color}", font = 11).pack(side = "left", padx = (8, 0))

def update_accent_colors():
    winaccent.update_accent_colors()
    for widget in window.winfo_children(): widget.destroy()

    add_item(winaccent.accent_light, "Light mode accent color")
    add_item(winaccent.accent_dark, "Dark mode accent color")
    add_item(winaccent.accent_normal, "Normal accent color")

    ttk.Button(window, text = "Refresh", command = update_accent_colors, default = "active").pack(fill = "x", pady = 8, padx = 5)

update_accent_colors()

window.mainloop()