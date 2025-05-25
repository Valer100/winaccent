import tkinter as tk, winaccent, ctypes, threading, argparse, traceback
from tkinter import ttk

color_item_index = -1

def gui_demo():
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("winaccent.demo")

    window = tk.Tk()
    window.title(f"winaccent {winaccent.__version__}")
    window.resizable(False, False)
    window.configure(padx = 10, pady = 10)

    full_palette = tk.BooleanVar(value = True)
    get_accent_from_dwm = tk.BooleanVar(value = False)
    dark_mode_window = tk.BooleanVar(value = False)

    icon = tk.PhotoImage(data = "iVBORw0KGgoAAAANSUhEUgAAAEwAAABMBAMAAAA1uUwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAYUExURQAAAAAaaAA+kgBnwAB41ACR+EzC/5nr/8MyyRkAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAA9SURBVEjH7coxAQAQFEXRLwIRiEAEIhCB1aa+l4LlnvnYH85LiJKylCqty5iyjmwajUaj0Wg0Gu19e87sAnxWiuenyOclAAAAAElFTkSuQmCC")
    window.iconphoto(True, icon)

    style = ttk.Style()
    style.configure("TCheckbutton", font = ("Default", 11))
    style.configure("TNotebook", background = "SystemButtonFace")
    style.configure(".", background = "SystemWindow")

    notebook = ttk.Notebook(window, width = 300)
    notebook.pack()

    def lock_size():
        window.update()
        window.geometry("")
        window.update()
        window.geometry(window.geometry())

    def add_color(parent, color_name, color):
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

    def add_boolean_value(parent, value_name, value):
        style.map("Value.TCheckbutton", foreground = [("disabled", "SystemButtonText")])

        checkbutton = ttk.Checkbutton(parent, text = " " + value_name, style = "Value.TCheckbutton")
        checkbutton.pack(anchor = "w", pady = (0, 4))
        checkbutton.invoke()
        checkbutton.configure(state = "disabled")

        if value: checkbutton.state(["selected"])
        else: checkbutton.state(["!selected"])

    accent_palette = ttk.Frame(notebook, padding = 10)
    notebook.add(accent_palette, text = "Accent palette")

    def update_accent_palette_colors():
        global color_item_index

        for widget in accent_palette.winfo_children(): widget.destroy()
        winaccent.get_accent_from_dwm = get_accent_from_dwm.get()
        winaccent.update_values()

        header = ttk.Frame(accent_palette)
        header.pack(anchor = "w", fill = "x")

        ttk.Label(header, text = "Accent palette", font = ("Segoe UI Semibold", 15)).pack(pady = (0, 10), anchor = "w", side = "left")
        ttk.Checkbutton(header, text = " Full palette", variable = full_palette, command = update_accent_palette_colors).pack(anchor = "w", pady = (0, 5), side = "right")

        current_text_color_rgb = window.winfo_rgb("SystemButtonText")
        current_text_color = f"#{current_text_color_rgb[0]:02x}{current_text_color_rgb[1]:02x}{current_text_color_rgb[2]:02x}"
        palette_bd = winaccent.accent_dark_3 if winaccent._utils.white_text_on_color(current_text_color) else winaccent.accent_light_3

        accent_palette_colors = tk.Frame(accent_palette, highlightbackground = palette_bd, highlightcolor = palette_bd, highlightthickness = 1)
        accent_palette_colors.pack(anchor = "w", fill = "both", expand = True)

        if full_palette.get():
            accent_palette_colors.grid_rowconfigure(0, weight = 1)
            accent_palette_colors.grid_rowconfigure(1, weight = 1)
            accent_palette_colors.grid_rowconfigure(2, weight = 1)
            accent_palette_colors.grid_rowconfigure(3, weight = 1)
            accent_palette_colors.grid_rowconfigure(4, weight = 1)
            accent_palette_colors.grid_rowconfigure(5, weight = 1)
            accent_palette_colors.grid_rowconfigure(6, weight = 1)

            add_color(accent_palette_colors, "accent_light_3", winaccent.accent_light_3)
            add_color(accent_palette_colors, "accent_light_2", winaccent.accent_light_2)
            add_color(accent_palette_colors, "accent_light_1", winaccent.accent_light_1)
            add_color(accent_palette_colors, "accent_normal", winaccent.accent_normal)
            add_color(accent_palette_colors, "accent_dark_1", winaccent.accent_dark_1)
            add_color(accent_palette_colors, "accent_dark_2", winaccent.accent_dark_2)
            add_color(accent_palette_colors, "accent_dark_3", winaccent.accent_dark_3)
        else:
            accent_palette_colors.grid_rowconfigure(0, weight = 1)
            accent_palette_colors.grid_rowconfigure(1, weight = 1)
            accent_palette_colors.grid_rowconfigure(2, weight = 1)
            accent_palette_colors.grid_rowconfigure(3, weight = 0)
            accent_palette_colors.grid_rowconfigure(4, weight = 0)
            accent_palette_colors.grid_rowconfigure(5, weight = 0)
            accent_palette_colors.grid_rowconfigure(6, weight = 0)

            add_color(accent_palette_colors, "accent_light", winaccent.accent_light)
            add_color(accent_palette_colors, "accent_normal", winaccent.accent_normal)
            add_color(accent_palette_colors, "accent_dark", winaccent.accent_dark)

        color_item_index = -1

        ttk.Label(accent_palette, text = "Other colors", font = ("Segoe UI Semibold", 15)).pack(pady = (16, 10), anchor = "w")

        accent_menu = tk.Frame(accent_palette, highlightbackground = "SystemButtonText", highlightcolor = "SystemButtonText", highlightthickness = 1)
        accent_menu.pack(anchor = "w", fill = "x")

        add_color(accent_menu, "accent_menu", winaccent.accent_menu)
        color_item_index = -1

        ttk.Label(accent_palette, text = "Flags", font = ("Segoe UI Semibold", 15)).pack(pady = (16, 6), anchor = "w")
        ttk.Checkbutton(accent_palette, text = " get_accent_from_dwm", variable = get_accent_from_dwm, command = update_accent_palette_colors).pack(anchor = "w", padx = 4)


    window_chrome = ttk.Frame(notebook, padding = 10)
    notebook.add(window_chrome, text = "Window chrome")

    def update_windows_chrome_colors():
        global color_item_index

        for widget in window_chrome.winfo_children(): widget.destroy()
        winaccent.dark_mode_window = dark_mode_window.get()
        winaccent.update_values()

        ttk.Label(window_chrome, text = "Titlebar", font = ("Segoe UI Semibold", 15)).pack(pady = (0, 6), anchor = "w")
        add_boolean_value(window_chrome, "is_titlebar_colored", winaccent.is_titlebar_colored)

        ttk.Label(window_chrome, text = "Active window", font = ("Segoe UI Semibold", 15)).pack(pady = (12, 10), anchor = "w")

        active_window_colors = tk.Frame(window_chrome, highlightbackground = "SystemButtonText", highlightcolor = "SystemButtonText", highlightthickness = 1)
        active_window_colors.pack(anchor = "w", fill = "x")

        add_color(active_window_colors, "titlebar_active", winaccent.titlebar_active)
        add_color(active_window_colors, "titlebar_active_text", winaccent.titlebar_active_text)
        add_color(active_window_colors, "window_border_active", winaccent.window_border_active)

        color_item_index = -1

        ttk.Label(window_chrome, text = "Inactive window", font = ("Segoe UI Semibold", 15)).pack(pady = (16, 10), anchor = "w")

        inactive_window_colors = tk.Frame(window_chrome, highlightbackground = "SystemButtonText", highlightcolor = "SystemButtonText", highlightthickness = 1)
        inactive_window_colors.pack(anchor = "w", fill = "x")

        add_color(inactive_window_colors, "titlebar_inactive", winaccent.titlebar_inactive)
        add_color(inactive_window_colors, "titlebar_inactive_text", winaccent.titlebar_inactive_text)
        add_color(inactive_window_colors, "window_border_inactive", winaccent.window_border_inactive)

        color_item_index = -1

        ttk.Label(window_chrome, text = "Flags", font = ("Segoe UI Semibold", 15)).pack(pady = (16, 6), anchor = "w")
        ttk.Checkbutton(window_chrome, text = " dark_mode_window", variable = dark_mode_window, command = update_windows_chrome_colors).pack(anchor = "w", padx = 4)


    system = ttk.Frame(notebook, padding = 10)
    notebook.add(system, text = "System")

    def update_system_info():
        global color_item_index
        for widget in system.winfo_children(): widget.destroy()

        ttk.Label(system, text = "Start Menu", font = ("Segoe UI Semibold", 15)).pack(pady = (0, 6), anchor = "w")
        add_boolean_value(system, "is_start_menu_colored", winaccent.is_start_menu_colored)
        
        start_menu_color = tk.Frame(system, highlightbackground = "SystemButtonText", highlightcolor = "SystemButtonText", highlightthickness = 1)
        start_menu_color.pack(anchor = "w", fill = "x", pady = (8, 0))
        
        add_color(start_menu_color, "start_menu", winaccent.start_menu)
        color_item_index = -1

        ttk.Label(system, text = "Taskbar", font = ("Segoe UI Semibold", 15)).pack(pady = (16, 6), anchor = "w")
        add_boolean_value(system, "is_taskbar_colored", winaccent.is_taskbar_colored)

        taskbar_color = tk.Frame(system, highlightbackground = "SystemButtonText", highlightcolor = "SystemButtonText", highlightthickness = 1)
        taskbar_color.pack(anchor = "w", fill = "x", pady = (8, 0))

        add_color(taskbar_color, "taskbar", winaccent.taskbar)
        color_item_index = -1

        ttk.Label(system, text = "UI Appearance", font = ("Segoe UI Semibold", 15)).pack(pady = (16, 6), anchor = "w")

        add_boolean_value(system, "transparency_effects_enabled", winaccent.transparency_effects_enabled)
        add_boolean_value(system, "apps_use_light_theme", winaccent.apps_use_light_theme)
        add_boolean_value(system, "system_uses_light_theme", winaccent.system_uses_light_theme)

    def on_appearance_changed(event):
        if event == winaccent.event.accent_color_changed: update_accent_palette_colors()
        elif event == winaccent.event.window_chrome_color_changed: update_windows_chrome_colors()
        elif event == winaccent.event.system_theme_changed: update_system_info()
        elif event == winaccent.event.transparency_effects_toggled: update_system_info()
        elif event == winaccent.event.start_menu_color_changed: update_system_info()
        elif event == winaccent.event.taskbar_color_changed: update_system_info()

    update_accent_palette_colors()
    update_windows_chrome_colors()
    update_system_info()

    thread = threading.Thread(target = lambda: winaccent.on_appearance_changed(callback = on_appearance_changed, pass_event = True), daemon = True)
    thread.start()

    lock_size()
    window.mainloop()


def console_demo():
    print(f"\nwinaccent {winaccent.__version__}")
    print("=" * len(f"winaccent {winaccent.__version__}") + "\n")

    print("\nAccent palette")
    print("--------------\n")

    print(f"accent_light_3:                 {winaccent.accent_light_3}")
    print(f"accent_light_2:                 {winaccent.accent_light_2}")
    print(f"accent_light_1:                 {winaccent.accent_light_1}")
    print(f"accent_normal:                  {winaccent.accent_normal}")
    print(f"accent_dark_1:                  {winaccent.accent_dark_1}")
    print(f"accent_dark_2:                  {winaccent.accent_dark_2}")
    print(f"accent_dark_3:                  {winaccent.accent_dark_3}")

    print("\n\nWindow chrome")
    print("-------------\n")
    

    print(f"is_titlebar_colored:            {winaccent.is_titlebar_colored}")
    print(f"titlebar_active:                {winaccent.titlebar_active}")
    print(f"titlebar_active_text:           {winaccent.titlebar_active_text}")
    print(f"titlebar_inactive:              {winaccent.titlebar_inactive}")
    print(f"titlebar_inactive_text:         {winaccent.titlebar_inactive_text}")
    print(f"window_border_active:           {winaccent.window_border_active}")
    print(f"window_border_inactive:         {winaccent.window_border_inactive}")
    
    print("\n\nStart Menu")
    print("----------\n")

    print(f"is_start_menu_colored:          {winaccent.is_start_menu_colored}")
    print(f"start_menu:                     {winaccent.start_menu}")

    print("\n\nTaskbar")
    print("-------\n")

    print(f"is_taskbar_colored:             {winaccent.is_taskbar_colored}")
    print(f"taskbar:                        {winaccent.taskbar}")

    print("\n\nUI Appearance")
    print("-------------\n")

    print(f"transparency_effects_enabled:   {winaccent.transparency_effects_enabled}")
    print(f"apps_use_light_theme:           {winaccent.apps_use_light_theme}")
    print(f"system_uses_light_theme:        {winaccent.system_uses_light_theme}")

    print("\n\nOther colors")
    print("------------\n")

    print(f"accent_menu:                    {winaccent.accent_menu}")
    print("\n")


parser = argparse.ArgumentParser(usage = "python -m winaccent --mode")
parser.add_argument("--mode", type = str, required = False, choices = ["gui", "console", "auto"], metavar = "", help = "choose the demo mode. Accepted values: gui, console, auto.")
arguments = parser.parse_args()

if arguments.mode == None or arguments.mode == "auto":
    try:
        gui_demo()
    except Exception as e:
        print("\nFailed to show GUI demo. Here's why:\n")
        traceback.print_exception(type(e), e, e.__traceback__)
        print("\nConsole demo will be shown instead.")
        console_demo()
elif arguments.mode == "gui": gui_demo()
elif arguments.mode == "console": console_demo()