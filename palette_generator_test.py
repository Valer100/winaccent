import tkinter as tk, ctypes
from tkinter import ttk, colorchooser
from winaccent import _utils
    
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("winaccent.demo")

window = tk.Tk()
window.title("Palette generator")
window.resizable(False, False)
window.configure(padx = 8, pady = 8)

accent_normal = "#4617b4"

icon = tk.PhotoImage(data = "iVBORw0KGgoAAAANSUhEUgAAAEwAAABMBAMAAAA1uUwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAYUExURQAAAAAaaAA+kgBnwAB41ACR+EzC/5nr/8MyyRkAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAA9SURBVEjH7coxAQAQFEXRLwIRiEAEIhCB1aa+l4LlnvnYH85LiJKylCqty5iyjmwajUaj0Wg0Gu19e87sAnxWiuenyOclAAAAAElFTkSuQmCC")
window.iconphoto(True, icon)

style = ttk.Style()
style.configure("TButton", font = 11)

ttk.Label(window, text = "Main color", font = ("Segoe UI Semibold", 15)).pack(padx = 8, pady = (0, 8), anchor = "w")

color = ttk.Frame(window)
color.pack(fill = "x", anchor = "w", padx = 8)

color_prev = tk.Frame(color, width = 20, height = 20, highlightthickness = 1, highlightbackground = "#000000", bg = accent_normal)
color_prev.pack(side = "left")

def on_color_change(event = None):
    if len(color_input.get()) == 7:
        try: color_prev["bg"] = color_input.get(); update_palette()
        except: color_prev["bg"] = "SystemMenu"
    else:
        color_prev["bg"] = "SystemMenu"

def choose_color():
    global accent_normal
    accent_normal = colorchooser.askcolor()[1].upper()
    
    color_input.delete(0, "end")
    color_input.insert(0, accent_normal)

    on_color_change()

color_input = ttk.Entry(color, font = ("Consolas", 11))
color_input.pack(side = "left", padx = 8, fill = "x", expand = True)
color_input.focus_set()
color_input.insert(0, accent_normal)
color_input.bind("<KeyRelease>", on_color_change)

pick_color = ttk.Button(color, text = "...", width = 3, command = choose_color).pack(side = "left")

palette = ttk.Frame(window)
palette.pack(anchor = "w")

def add_item(color, text):
    color_item = tk.Frame(palette, padx = 8, pady = 0)
    color_item.pack(pady = 2, anchor = "w")

    color_prev = tk.Frame(color_item, width = 20, height = 20, highlightthickness = 1, highlightbackground = "SystemMenu")
    color_prev.pack(side = "left")

    try: color_prev.configure(bg = color, highlightbackground = "#000000")
    except: pass
    
    ttk.Label(color_item, text = text, font = ("Default", 11), width = 23).pack(side = "left", padx = (8, 0), anchor = "w")
    
    color_value = tk.Text(color_item, width = 7, height = 1, font = ("Consolas", 11), bd = 0, bg = ttk.Style().lookup(".", "background"))
    color_value.pack(side = "right")
    color_value.insert("1.0", str(color))
    color_value["state"] = "disabled"

def update_palette():
    accent_light_3 = _utils.increase_saturation(_utils.blend_colors("#FFFFFF", accent_normal, 75), 2)
    accent_light_2 = _utils.increase_saturation(_utils.blend_colors("#FFFFFF", accent_normal, 50), 2)
    accent_light_1 = _utils.increase_saturation(_utils.blend_colors("#FFFFFF", accent_normal, 25), 2)
    accent_dark_1 = _utils.increase_saturation(_utils.blend_colors("#000000", accent_normal, 25), 2)
    accent_dark_2 = _utils.increase_saturation(_utils.blend_colors("#000000", accent_normal, 50), 2)
    accent_dark_3 = _utils.increase_saturation(_utils.blend_colors("#000000", accent_normal, 75), 2)

    for widget in palette.winfo_children(): widget.destroy()
    ttk.Label(palette, text = "Generated palette", font = ("Segoe UI Semibold", 15)).pack(padx = 8, pady = (16, 8), anchor = "w")

    add_item(accent_light_3, "accent_light_3")
    add_item(accent_light_2, "accent_light_2")
    add_item(accent_light_1, "accent_light_1")
    add_item(accent_normal, "accent_normal")
    add_item(accent_dark_1, "accent_dark_1")
    add_item(accent_dark_2, "accent_dark_2")
    add_item(accent_dark_3, "accent_dark_3")

update_palette()
window.mainloop()