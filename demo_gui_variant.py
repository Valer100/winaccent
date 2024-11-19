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

    color_item = tk.Frame(parent, bg = color, padx = 8, pady = 8)
    color_item.pack(fill = "x")

    color_name = tk.Label(color_item, text = color_name, font = ("Default", 11), fg = text_color, bg = color)
    color_name.pack(side = "left")

    color_value = tk.Text(color_item, width = 7, height = 1, font = ("Consolas", 11), bd = 0, bg = color, fg = text_color, 
                          selectbackground = text_color, selectforeground = text_color_inverse)
    color_value.pack(side = "right")
    color_value.insert("1.0", str(color))
    color_value["state"] = "disabled"

def add_boolean_value(parent, value_name, value):
    style.map("Value.TCheckbutton", foreground = [("disabled", "SystemButtonText")])

    checkbutton = ttk.Checkbutton(parent, text = " " + value_name, style = "Value.TCheckbutton")
    checkbutton.pack(anchor = "w", pady = (4, 0))
    checkbutton.invoke()
    checkbutton.configure(state = "disabled")

    if value: checkbutton.state(["selected"])
    else: checkbutton.state(["!selected"])

accent_palette = ttk.Frame(notebook, padding = 10)
notebook.add(accent_palette, text = "Accent palette")

def update_accent_palette():
    for widget in accent_palette.winfo_children(): widget.destroy()
    winaccent.get_accent_from_dwm = get_accent_from_dwm.get()

    ttk.Label(accent_palette, text = "Accent palette", font = ("Segoe UI Semibold", 15)).pack(pady = (0, 10), anchor = "w")
    
    accent_palette_colors = tk.Frame(accent_palette, highlightbackground = winaccent.accent_dark_3, highlightthickness = 1)
    accent_palette_colors.pack(anchor = "w", fill = "x")

    add_color(accent_palette_colors, "accent_light_3", winaccent.accent_light_3)
    add_color(accent_palette_colors, "accent_light_2", winaccent.accent_light_2)
    add_color(accent_palette_colors, "accent_light_1", winaccent.accent_light_1)
    add_color(accent_palette_colors, "accent_normal", winaccent.accent_normal)
    add_color(accent_palette_colors, "accent_dark_1", winaccent.accent_dark_1)
    add_color(accent_palette_colors, "accent_dark_2", winaccent.accent_dark_2)
    add_color(accent_palette_colors, "accent_dark_3", winaccent.accent_dark_3)

    ttk.Label(accent_palette, text = "Other colors", font = ("Segoe UI Semibold", 15)).pack(pady = (16, 10), anchor = "w")
    
    accent_menu = tk.Frame(accent_palette, highlightbackground = "SystemButtonText", highlightthickness = 1)
    accent_menu.pack(anchor = "w", fill = "x")

    add_color(accent_menu, "accent_menu", winaccent.accent_menu)

    ttk.Label(accent_palette, text = "Flags", font = ("Segoe UI Semibold", 15)).pack(pady = (16, 10), anchor = "w")
    ttk.Checkbutton(accent_palette, text = " get_accent_from_dwm", variable = get_accent_from_dwm, command = update_accent_palette).pack(anchor = "w", padx = 4)


window_chrome = ttk.Frame(notebook, padding = 10)
notebook.add(window_chrome, text = "Window chrome")

def update_windows_preview():
    for widget in window_chrome.winfo_children(): widget.destroy()
    winaccent.dark_mode_titlebar = dark_mode_titlebar.get()
    winaccent.update_values()

    add_boolean_value(window_chrome, "is_titlebar_colored", winaccent.is_titlebar_colored)

    ttk.Label(window_chrome, text = "Active window", font = ("Segoe UI Semibold", 15)).pack(pady = (16, 10), anchor = "w")

    active_window_colors = tk.Frame(window_chrome, highlightbackground = "SystemButtonText", highlightthickness = 1)
    active_window_colors.pack(anchor = "w", fill = "x")

    add_color(active_window_colors, "titlebar_active", winaccent.titlebar_active)
    add_color(active_window_colors, "titlebar_active_text", winaccent.titlebar_active_text)
    add_color(active_window_colors, "window_border_active", winaccent.window_border_active)

    ttk.Label(window_chrome, text = "Inactive window", font = ("Segoe UI Semibold", 15)).pack(pady = (16, 10), anchor = "w")

    inactive_window_colors = tk.Frame(window_chrome, highlightbackground = "SystemButtonText", highlightthickness = 1)
    inactive_window_colors.pack(anchor = "w", fill = "x")

    add_color(inactive_window_colors, "titlebar_inactive", winaccent.titlebar_inactive)
    add_color(inactive_window_colors, "titlebar_inactive_text", winaccent.titlebar_inactive_text)
    add_color(inactive_window_colors, "window_border_inactive", winaccent.window_border_inactive)

    ttk.Label(window_chrome, text = "Flags", font = ("Segoe UI Semibold", 15)).pack(pady = (16, 10), anchor = "w")
    ttk.Checkbutton(window_chrome, text = " dark_mode_titlebar", variable = dark_mode_titlebar, command = update_windows_preview).pack(anchor = "w", padx = 4)
    

theme = ttk.Frame(notebook, padding = 10)
notebook.add(theme, text = "Theme")

def update_theme():
    for widget in theme.winfo_children(): widget.destroy()

    ttk.Label(theme, text = "Theme", font = ("Segoe UI Semibold", 15)).pack(pady = (0, 6), anchor = "w")

    add_boolean_value(theme, "apps_use_light_theme", winaccent.apps_use_light_theme)
    add_boolean_value(theme, "system_uses_light_theme", winaccent.system_uses_light_theme)

def on_appearance_changed(event):
    if event == winaccent.event.accent_color_changed: update_accent_palette()
    elif event == winaccent.event.window_chrome_color_changed: update_windows_preview()
    elif event == winaccent.event.system_theme_changed: update_theme()

update_accent_palette()
update_windows_preview()
update_theme()

thread = threading.Thread(target = lambda: winaccent.on_appearance_changed(callback = on_appearance_changed, pass_event = True), daemon = True)
thread.start()

lock_size()
window.mainloop()