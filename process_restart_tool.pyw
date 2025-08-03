import tkinter as tk, subprocess, ctypes, os
from tkinter import ttk

os.chdir(os.path.dirname(__file__))

try:
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("winaccent.demo")
except:
    pass

try:
    import winaccent
    apps_use_light_theme = winaccent.apps_use_light_theme
except:
    apps_use_light_theme = False

window = tk.Tk()
window.withdraw()
window.title("Process restart tool")
window.resizable(False, False)
window.configure(padx = 16, pady = 14)
window.iconbitmap("winaccent/icon.ico")

if not apps_use_light_theme:
    window.update()
    window.configure(background = "#202020")

    ctypes.windll.dwmapi.DwmSetWindowAttribute(
        ctypes.windll.user32.GetParent(window.winfo_id()), 20, ctypes.byref(ctypes.c_int(1)), 
        ctypes.sizeof(ctypes.c_int(1))
    )

    style = ttk.Style()

    style.element_create("Dark.Button.border", "from", "clam")
    style.layout("TButton", [("Dark.Button.border", {"sticky": "nswe", "border": "1", "children": [("Button.focus", {"sticky": "nswe", "children": [("Button.padding", {"sticky": "nswe", "children": [("Button.label", {"sticky": "nswe"})]})]})]})])
    style.configure("TButton", background = "#333333", bordercolor = "#9B9B9B", borderwidth = 1, relief = "raised")
    
    style.map("TButton",
        background = [("pressed", "#676767"), ("active", "#454545"), ("", "#333333")],
        lightcolor = [("pressed", "#676767"), ("active", "#454545"), ("", "#333333")],
        darkcolor = [("pressed", "#676767"), ("active", "#454545"), ("", "#333333")],
    )

    style.configure(".", background = "#202020", foreground = "#FFFFFF")

ttk.Label(window, text = "Click one of the following buttons to restart a process").pack(anchor = "w", pady = (0, 14))
ttk.Button(window, text = "Restart explorer.exe", command = lambda: subprocess.call("taskkill /f /im explorer.exe & start explorer", shell = True)).pack(fill = "x")
ttk.Button(window, text = "Restart dwm.exe", command = lambda: ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd", "/c taskkill /f /im dwm.exe", "", 1)).pack(fill = "x", pady = (4 if apps_use_light_theme else 8, 0))

window.deiconify()
window.mainloop()