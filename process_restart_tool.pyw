import tkinter as tk, subprocess, ctypes, os
from tkinter import ttk

os.chdir(os.path.dirname(__file__))

try:
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("winaccent.demo")
except:
    pass

window = tk.Tk()
window.title("Process restart tool")
window.resizable(False, False)
window.configure(padx = 16, pady = 14)
window.iconbitmap("winaccent/icon.ico")

ttk.Label(window, text = "Click one of the following buttons to restart a process").pack(anchor = "w", pady = (0, 14))
ttk.Button(window, text = "Restart explorer.exe", command = lambda: subprocess.call("taskkill /f /im explorer.exe & start explorer", shell = True)).pack(fill = "x")
ttk.Button(window, text = "Restart dwm.exe", command = lambda: ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd", "/c taskkill /f /im dwm.exe", "", 1)).pack(fill = "x", pady = (4, 0))

window.mainloop()