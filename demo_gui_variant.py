import tkinter as tk, ctypes, winaccent, threading
from tkinter import ttk

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("winaccent.demo")

window = tk.Tk()
window.title("winaccent")
window.resizable(False, False)
window.configure(padx = 10, pady = 10)
    
get_accent_from_dwm = tk.BooleanVar(value = False)
dark_mode_titlebar = tk.BooleanVar(value = False)

icon = tk.PhotoImage(data = "iVBORw0KGgoAAAANSUhEUgAAAEwAAABMBAMAAAA1uUwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAYUExURQAAAAAaaAA+kgBnwAB41ACR+EzC/5nr/8MyyRkAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAA9SURBVEjH7coxAQAQFEXRLwIRiEAEIhCB1aa+l4LlnvnYH85LiJKylCqty5iyjmwajUaj0Wg0Gu19e87sAnxWiuenyOclAAAAAElFTkSuQmCC")
window.iconphoto(True, icon)

style = ttk.Style()
style.configure("TCheckbutton", font = ("Default", 11))

notebook = ttk.Notebook(window, width = 300)
notebook.pack()

def lock_size():
    window.update()
    window.geometry("")
    window.update()
    window.geometry(window.geometry())

def add_color(parent, color_name, color):
    text_color = "#FFFFFF" if winaccent._utils.white_text_on_color(color) else "#000000"
    text_color_inverse = "#000000" if winaccent._utils.white_text_on_color(color) else "#FFFFFF"

    color_item = tk.Frame(parent, bg = color, padx = 4, pady = 4)
    color_item.pack(expand = True, fill = "x")

    color_name = tk.Label(color_item, text = color_name, font = ("Default", 11), fg = text_color, bg = color)
    color_name.pack(side = "left")

    color_value = tk.Text(color_item, width = 7, height = 1, font = ("Consolas", 11), bd = 0, bg = color, fg = text_color, 
                          selectbackground = text_color, selectforeground = text_color_inverse)
    color_value.pack(side = "right")
    color_value.insert("1.0", str(color))
    color_value["state"] = "disabled"


accent_palette = ttk.Frame(notebook, padding = 10)
notebook.add(accent_palette, text = "Accent palette")

def update_accent_palette():
    for widget in accent_palette.winfo_children(): widget.destroy()
    winaccent.get_accent_from_dwm = get_accent_from_dwm.get()

    accent_palette_frame = ttk.Frame(accent_palette)
    accent_palette_frame.pack(expand = True, fill = "x", anchor = "nw")

    ttk.Label(accent_palette_frame, text = "Accent palette", font = ("Segoe UI Semibold", 15)).pack(pady = (0, 8), anchor = "w")
    add_color(accent_palette_frame, "accent_light_3", winaccent.accent_light_3)
    add_color(accent_palette_frame, "accent_light_2", winaccent.accent_light_2)
    add_color(accent_palette_frame, "accent_light_1", winaccent.accent_light_1)
    add_color(accent_palette_frame, "accent_normal", winaccent.accent_normal)
    add_color(accent_palette_frame, "accent_dark_1", winaccent.accent_dark_1)
    add_color(accent_palette_frame, "accent_dark_2", winaccent.accent_dark_2)
    add_color(accent_palette_frame, "accent_dark_3", winaccent.accent_dark_3)

    ttk.Label(accent_palette_frame, text = "Other colors", font = ("Segoe UI Semibold", 15)).pack(pady = (16, 8), anchor = "w")
    add_color(accent_palette_frame, "accent_menu", winaccent.accent_menu)

    ttk.Label(accent_palette_frame, text = "Flags", font = ("Segoe UI Semibold", 15)).pack(pady = (16, 8), anchor = "w")
    ttk.Checkbutton(accent_palette_frame, text = " get_accent_from_dwm", variable = get_accent_from_dwm, command = update_accent_palette).pack(anchor = "w", padx = 4)


window_chrome = ttk.Frame(notebook, padding = 10)
notebook.add(window_chrome, text = "Window chrome")

def update_windows_preview():
    for widget in window_chrome.winfo_children(): widget.destroy()
    winaccent.dark_mode_titlebar = dark_mode_titlebar.get()
    winaccent.update_values()

    window_bg = "#F0F0F0" if not dark_mode_titlebar.get() else "#202020"

    ttk.Label(window_chrome, text = "Active window", font = ("Segoe UI Semibold", 15)).pack(pady = (0, 16), anchor = "w")

    active_window = tk.Frame(window_chrome, bg = window_bg, highlightthickness = 1, 
                             highlightcolor = winaccent.window_border_active, 
                             highlightbackground = winaccent.window_border_active, 
                             width = 300, height = 150)
    active_window.pack()
    active_window.pack_propagate(False)

    active_titlebar = tk.Frame(active_window, bg = winaccent.titlebar_active)
    active_titlebar.pack(fill = "x", expand = True, anchor = "nw")

    ttk.Label(active_titlebar, text = "Active window", foreground = winaccent.titlebar_active_text, 
              background = winaccent.titlebar_active).pack(padx = (8, 0), pady = 5, side = "left")
    
    ttk.Label(active_titlebar, text = "\ue921      \ue922      \ue8bb   ", font = ("Segoe MDL2 Assets", 8), foreground = winaccent.titlebar_active_text, 
              background = winaccent.titlebar_active).pack(pady = 5, side = "right")

    active_window_content = tk.Frame(active_window, bg = window_bg, highlightthickness = 1, 
                                     highlightbackground = "#9e9e9e",
                                     highlightcolor = "#9e9e9e")
    active_window_content.pack(expand = True, fill = "x", padx = 16, pady = 8)

    add_color(active_window_content, "titlebar_active", winaccent.titlebar_active)
    add_color(active_window_content, "titlebar_active_text", winaccent.titlebar_active_text)
    add_color(active_window_content, "window_border_active", winaccent.window_border_active)


    ttk.Label(window_chrome, text = "Inactive window", font = ("Segoe UI Semibold", 15)).pack(pady = 16, anchor = "w")

    inactive_window = tk.Frame(window_chrome, bg = window_bg, highlightthickness = 1, 
                               highlightcolor = winaccent.window_border_inactive, 
                               highlightbackground = winaccent.window_border_inactive, 
                               width = 300, height = 150)
    inactive_window.pack()
    inactive_window.pack_propagate(False)

    inactive_titlebar = tk.Frame(inactive_window, bg = winaccent.titlebar_inactive)
    inactive_titlebar.pack(fill = "x", expand = True, anchor = "nw")

    ttk.Label(inactive_titlebar, text = "Inactive window", foreground = winaccent.titlebar_inactive_text, 
              background = winaccent.titlebar_inactive).pack(padx = (8, 0), pady = 5, side = "left")
    
    ttk.Label(inactive_titlebar, text = "\ue921      \ue922      \ue8bb   ", font = ("Segoe MDL2 Assets", 8), 
              foreground = winaccent.titlebar_inactive_text, background = winaccent.titlebar_inactive).pack(pady = 5, side = "right")

    inactive_window_content = tk.Frame(inactive_window, bg = window_bg, highlightthickness = 1, 
                                     highlightbackground = "#9e9e9e",
                                     highlightcolor = "#9e9e9e")
    inactive_window_content.pack(expand = True, fill = "x", padx = 16, pady = 8)

    add_color(inactive_window_content, "titlebar_inactive", winaccent.titlebar_inactive)
    add_color(inactive_window_content, "titlebar_inactive_text", winaccent.titlebar_inactive_text)
    add_color(inactive_window_content, "window_border_inactive", winaccent.window_border_inactive)


    ttk.Label(window_chrome, text = "Flags", font = ("Segoe UI Semibold", 15)).pack(pady = (16, 8), anchor = "w")
    ttk.Checkbutton(window_chrome, text = " dark_mode_titlebar", variable = dark_mode_titlebar, command = update_windows_preview).pack(anchor = "w", padx = 4)

def on_appearance_changed():
    update_accent_palette()
    update_windows_preview()

update_accent_palette()
update_windows_preview()

thread = threading.Thread(target = lambda: winaccent.on_appearance_changed(callback = on_appearance_changed), daemon = True)
thread.start()

lock_size()
window.mainloop()