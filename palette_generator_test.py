import tkinter as tk, ctypes, winaccent
from tkinter import ttk, colorchooser
    
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("winaccent.demo")

window = tk.Tk()
window.title("Palette generator")
window.resizable(False, False)
window.configure(padx = 10, pady = 10)

def lock_geometry(window):
    if full_palette.get() != full_palette_old:
        window.geometry("")
        window.update()
        window.geometry(window.geometry())

accent_normal = "#4617B4"
accent_dark_3 = winaccent._utils.generate_color_palette(accent_normal)[5]

full_palette_old = False
full_palette = tk.BooleanVar(value = True)

icon = tk.PhotoImage(data = "iVBORw0KGgoAAAANSUhEUgAAAEwAAABMBAMAAAA1uUwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAYUExURQAAAAAaaAA+kgBnwAB41ACR+EzC/5nr/8MyyRkAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAA9SURBVEjH7coxAQAQFEXRLwIRiEAEIhCB1aa+l4LlnvnYH85LiJKylCqty5iyjmwajUaj0Wg0Gu19e87sAnxWiuenyOclAAAAAElFTkSuQmCC")
window.iconphoto(True, icon)

style = ttk.Style()
style.configure("TButton", font = 11)
style.configure("TCheckbutton", font = ("Default", 11))

ttk.Label(window, text = "Main color", font = ("Segoe UI Semibold", 15)).pack(padx = 8, pady = (0, 8), anchor = "w")

color = ttk.Frame(window)
color.pack(fill = "x", anchor = "w", padx = 10)

color_prev = tk.Frame(color, width = 23, height = 23, highlightthickness = 1, highlightbackground = accent_dark_3, bg = accent_normal)
color_prev.pack(side = "left")

def on_color_change(event = None):
    global accent_normal
    accent_normal = color_input.get().upper()

    if len(color_input.get()) == 7:
        try: color_prev["bg"] = accent_normal; update_palette()
        except: color_prev["bg"] = "SystemButtonFace"
    else:
        color_prev["bg"] = "SystemButtonFace"

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

ttk.Frame(window, width = 280).pack()

palette = ttk.Frame(window)
palette.pack(anchor = "w", fill = "x")

def add_item(parent, color, text):
    text_color = "#FFFFFF" if winaccent._utils.white_text_on_color(color) else "#000000"
    text_color_inverse = "#000000" if winaccent._utils.white_text_on_color(color) else "#FFFFFF"

    color_item = tk.Frame(parent, bg = color, padx = 8, pady = 6)
    color_item.pack(fill = "x")

    color_name = tk.Label(color_item, text = text, font = ("Default", 11), fg = text_color, bg = color)
    color_name.pack(side = "left")

    color_value = tk.Text(color_item, width = 7, height = 1, font = ("Consolas", 11), bd = 0, bg = color, fg = text_color, 
                          selectbackground = text_color, selectforeground = text_color_inverse)
    color_value.pack(side = "right")
    color_value.insert("1.0", str(color))
    color_value["state"] = "disabled"

def update_palette():
    global full_palette_old

    accent_palette = winaccent._utils.generate_color_palette(accent_normal)

    accent_light_3 = accent_palette[0]
    accent_light_2 = accent_palette[1]
    accent_light_1 = accent_palette[2]
    accent_dark_1 = accent_palette[3]
    accent_dark_2 = accent_palette[4]
    accent_dark_3 = accent_palette[5]

    for widget in palette.winfo_children(): widget.destroy()

    palette_header = ttk.Frame(palette)
    palette_header.pack(anchor = "w", fill = "x")

    ttk.Label(palette_header, text = "Palette", font = ("Segoe UI Semibold", 15)).pack(padx = (8, 0), pady = (16, 8), anchor = "w", side = "left")
    ttk.Checkbutton(palette_header, text = " Full palette", variable = full_palette, command = update_palette).pack(anchor = "w", pady = (13, 0), padx = (0, 8), side = "right")

    palette_colors = tk.Frame(palette, highlightbackground = accent_dark_3, highlightthickness = 1)
    palette_colors.pack(anchor = "w", fill = "x", padx = 8, pady = (0, 8))

    if full_palette.get():
        add_item(palette_colors, accent_light_3, "accent_light_3")
        add_item(palette_colors, accent_light_2, "accent_light_2")
        add_item(palette_colors, accent_light_1, "accent_light_1")
        add_item(palette_colors, accent_normal, "accent_normal")
        add_item(palette_colors, accent_dark_1, "accent_dark_1")
        add_item(palette_colors, accent_dark_2, "accent_dark_2")
        add_item(palette_colors, accent_dark_3, "accent_dark_3")
    else:
        add_item(palette_colors, accent_light_2, "accent_light")
        add_item(palette_colors, accent_normal, "accent_normal")
        add_item(palette_colors, accent_dark_1, "accent_dark")

    lock_geometry(window)
    full_palette_old = full_palette.get()

update_palette()
window.mainloop()