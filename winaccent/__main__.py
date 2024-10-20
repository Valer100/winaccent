import winaccent, threading, argparse

def gui_demo():
    import tkinter as tk, ctypes
    from tkinter import ttk
    
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("winaccent.demo")

    window = tk.Tk()
    window.title("winaccent")
    window.resizable(False, False)
    window.configure(padx = 8, pady = 8)
    
    icon = tk.PhotoImage(data = "iVBORw0KGgoAAAANSUhEUgAAAEwAAABMBAMAAAA1uUwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAYUExURQAAAAAaaAA+kgBnwAB41ACR+EzC/5nr/8MyyRkAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAA9SURBVEjH7coxAQAQFEXRLwIRiEAEIhCB1aa+l4LlnvnYH85LiJKylCqty5iyjmwajUaj0Wg0Gu19e87sAnxWiuenyOclAAAAAElFTkSuQmCC")
    window.iconphoto(True, icon)
    
    style = ttk.Style()
    style.configure("TButton", font = 11)
    
    def add_item(color, text):
        color_item = tk.Frame(window, padx = 8, pady = 0)
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
    
    def update():
        winaccent.update_values()
        for widget in window.winfo_children(): widget.destroy()
    
        ttk.Label(window, text = "Accent palette", font = ("Segoe UI Semibold", 15)).pack(padx = 8, pady = (0, 8), anchor = "w")

        add_item(winaccent.accent_light_3, "accent_light_3")
        add_item(winaccent.accent_light_2, "accent_light_2")
        add_item(winaccent.accent_light_1, "accent_light_1")
        add_item(winaccent.accent_normal, "accent_normal")
        add_item(winaccent.accent_dark_1, "accent_dark_1")
        add_item(winaccent.accent_dark_2, "accent_dark_2")
        add_item(winaccent.accent_dark_3, "accent_dark_3")

        ttk.Label(window, text = "Windows options", font = ("Segoe UI Semibold", 15)).pack(padx = 8, pady = (16, 8), anchor = "w")

        add_item(winaccent.is_titlebar_colored, "is_titlebar_colored")
        add_item(winaccent.titlebar_active, "titlebar_active")
        add_item(winaccent.titlebar_inactive, "titlebar_inactive")
        add_item(winaccent.window_border, "window_border")

        ttk.Label(window, text = "System theme", font = ("Segoe UI Semibold", 15)).pack(padx = 8, pady = (16, 8), anchor = "w")
        
        add_item(winaccent.apps_use_light_theme, "apps_use_light_theme")
        add_item(winaccent.system_uses_light_theme, "system_uses_light_theme")

        ttk.Label(window, text = "Other colors", font = ("Segoe UI Semibold", 15)).pack(padx = 8, pady = (16, 8), anchor = "w")

        add_item(winaccent.accent_menu, "accent_menu")
    
    update()
    
    thread = threading.Thread(target = lambda: winaccent.on_appearance_changed(update), daemon = True)
    thread.start()
    
    window.mainloop()

def console_demo():
    print("\nAccent palette")
    print("==============\n")

    print(f"accent_light_3:           {winaccent.accent_light_3}")
    print(f"accent_light_2:           {winaccent.accent_light_2}")
    print(f"accent_light_1:           {winaccent.accent_light_1}")
    print(f"accent_normal:            {winaccent.accent_normal}")
    print(f"accent_dark_1:            {winaccent.accent_dark_1}")
    print(f"accent_dark_2:            {winaccent.accent_dark_2}")
    print(f"accent_dark_3:            {winaccent.accent_dark_3}")

    print("\n\nWindows options")
    print("===============\n")
    

    print(f"is_titlebar_colored:      {winaccent.is_titlebar_colored}")
    print(f"titlebar_active:          {winaccent.titlebar_active}")
    print(f"titlebar_inactive:        {winaccent.titlebar_inactive}")
    print(f"window_border:            {winaccent.window_border}")
    
    print("\n\nSystem theme")
    print("============\n")

    print(f"apps_use_light_theme:     {winaccent.titlebar_inactive}")
    print(f"system_uses_light_theme:  {winaccent.window_border}")

    print("\n\nOther colors")
    print("============\n")

    print(f"accent_menu:              {winaccent.accent_menu}")
    print("\n")

parser = argparse.ArgumentParser(usage = "python -m winaccent --mode")
parser.add_argument("--mode", type = str, required = False, choices = ["gui", "console", "auto"], metavar = "", help = "choose the demo mode. Accepted values: gui, console, auto.")
arguments = parser.parse_args()

if arguments.mode == None or arguments.mode == "auto":
    try:
        gui_demo()
    except Exception as e:
        print(e)
        print("tkinter isn't available. Perhaps it isn't installed or the installation is corrupted.")
        console_demo()
elif arguments.mode == "gui": gui_demo()
elif arguments.mode == "console": console_demo()