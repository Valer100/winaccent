import tkinter as tk, winaccent

window = tk.Tk()
window.title("winaccent demo program")
window.resizable(False, False)
window.configure(padx = 8, pady = 4)

def add_item(color, text):
    color_item = tk.Frame(window, padx = 10, pady = 8)
    color_item.pack(pady = 4, anchor = "w")

    tk.Frame(color_item, width = 30, height = 30, bg = color, highlightthickness = 1, highlightbackground = "#000000").pack(side = "left")
    tk.Label(color_item, text = f"{text}: {color}", font = 11).pack(side = "left", padx = (8, 0))

add_item(winaccent.accent_auto, "Accent color based on theme")
add_item(winaccent.accent_light, "Light mode accent color")
add_item(winaccent.accent_dark, "Dark mode accent color")
add_item(winaccent.accent_normal, "Normal accent color")

window.mainloop()