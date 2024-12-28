import tkinter as tk, ctypes, winaccent
from tkinter import ttk, colorchooser
    
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("winaccent.demo")

window = tk.Tk()
window.title("Palette generator")
window.resizable(False, False)
window.configure(padx = 10, pady = 10)

color_item_index = -1
accent_normal = "#4617B4"
accent_dark_3 = winaccent._utils.generate_color_palette(accent_normal)[5]
accent_light_3 = winaccent._utils.generate_color_palette(accent_normal)[0]

full_palette = tk.BooleanVar(value = True)

icon = tk.PhotoImage(data = "iVBORw0KGgoAAAANSUhEUgAAAEwAAABMBAMAAAA1uUwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAYUExURQAAAAAaaAA+kgBnwAB41ACR+EzC/5nr/8MyyRkAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAA9SURBVEjH7coxAQAQFEXRLwIRiEAEIhCB1aa+l4LlnvnYH85LiJKylCqty5iyjmwajUaj0Wg0Gu19e87sAnxWiuenyOclAAAAAElFTkSuQmCC")
window.iconphoto(True, icon)

style = ttk.Style()
style.configure("TButton", font = 11)
style.configure("TCheckbutton", font = ("Default", 11))

ttk.Label(window, text = "Main color", font = ("Segoe UI Semibold", 15)).pack(padx = 8, pady = (0, 8), anchor = "w")

color = ttk.Frame(window)
color.pack(fill = "x", anchor = "w", padx = 10)

current_text_color_rgb = window.winfo_rgb("SystemButtonText")
current_text_color = f"#{current_text_color_rgb[0]:02x}{current_text_color_rgb[1]:02x}{current_text_color_rgb[2]:02x}"
palette_bd = accent_dark_3 if winaccent._utils.white_text_on_color(current_text_color) else accent_light_3

color_prev = tk.Frame(color, width = 23, height = 23, highlightthickness = 1, highlightbackground = palette_bd, bg = accent_normal)
color_prev.pack(side = "left")

def on_color_change(event = None):
    global accent_normal, palette_bd
    accent_normal = color_input.get().upper()

    if len(color_input.get()) == 7:
        try: 
            accent_dark_3 = winaccent._utils.generate_color_palette(accent_normal)[5]
            accent_light_3 = winaccent._utils.generate_color_palette(accent_normal)[0]

            current_text_color_rgb = window.winfo_rgb("SystemButtonText")
            current_text_color = f"#{current_text_color_rgb[0]:02x}{current_text_color_rgb[1]:02x}{current_text_color_rgb[2]:02x}"
            palette_bd = accent_dark_3 if winaccent._utils.white_text_on_color(current_text_color) else accent_light_3

            color_prev.configure(bg = accent_normal, highlightbackground = palette_bd)
            update_palette()
        except: 
            color_prev.configure(bg = "SystemButtonFace", highlightbackground = "SystemButtonText")
    else:
        color_prev.configure(bg = "SystemButtonFace", highlightbackground = "SystemButtonText")

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
palette.pack(anchor = "w", fill = "both", expand = True)

def add_color(parent, color, color_name):
    global color_item_index
    color_item_index += 1

    text_color = "#FFFFFF" if winaccent._utils.white_text_on_color(color) else "#000000"
    text_color_inverse = "#000000" if winaccent._utils.white_text_on_color(color) else "#FFFFFF"

    color_item = tk.Frame(parent, bg = color, padx = 8, pady = 6)
    color_item.grid(row = color_item_index, sticky = "nsew")

    parent.grid_columnconfigure(0, weight = 1)

    color_name = tk.Label(color_item, text = color_name, font = ("Default", 11), fg = text_color, bg = color)
    color_name.pack(side = "left")

    color_value = tk.Text(color_item, width = 7, height = 1, font = ("Consolas", 11), bd = 0, bg = color, fg = text_color, 
                          selectbackground = text_color, selectforeground = text_color_inverse)
    color_value.pack(side = "right")
    color_value.insert("1.0", str(color))
    color_value["state"] = "disabled"

def update_palette():
    global color_item_index, palette_bd
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

    palette_colors = tk.Frame(palette, highlightbackground = palette_bd, highlightthickness = 1, background = "#000000")
    palette_colors.pack(anchor = "w", fill = "both", expand = True, padx = 8, pady = (0, 8))

    if full_palette.get():
        palette_colors.grid_rowconfigure(0, weight = 1)
        palette_colors.grid_rowconfigure(1, weight = 1)
        palette_colors.grid_rowconfigure(2, weight = 1)
        palette_colors.grid_rowconfigure(3, weight = 1)
        palette_colors.grid_rowconfigure(4, weight = 1)
        palette_colors.grid_rowconfigure(5, weight = 1)
        palette_colors.grid_rowconfigure(6, weight = 1)

        add_color(palette_colors, accent_light_3, "accent_light_3")
        add_color(palette_colors, accent_light_2, "accent_light_2")
        add_color(palette_colors, accent_light_1, "accent_light_1")
        add_color(palette_colors, accent_normal, "accent_normal")
        add_color(palette_colors, accent_dark_1, "accent_dark_1")
        add_color(palette_colors, accent_dark_2, "accent_dark_2")
        add_color(palette_colors, accent_dark_3, "accent_dark_3")
    else:
        palette_colors.grid_rowconfigure(0, weight = 1)
        palette_colors.grid_rowconfigure(1, weight = 1)
        palette_colors.grid_rowconfigure(2, weight = 1)
        palette_colors.grid_rowconfigure(3, weight = 0)
        palette_colors.grid_rowconfigure(4, weight = 0)
        palette_colors.grid_rowconfigure(5, weight = 0)
        palette_colors.grid_rowconfigure(6, weight = 0)

        add_color(palette_colors, accent_light_2, "accent_light")
        add_color(palette_colors, accent_normal, "accent_normal")
        add_color(palette_colors, accent_dark_1, "accent_dark")

    color_item_index = -1

update_palette()

window.update()
window.geometry(window.geometry())

window.mainloop()