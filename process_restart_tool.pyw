import tkinter as tk, subprocess, ctypes, sys, os
from tkinter import ttk

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("winaccent.demo")

if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "\"" + os.path.abspath(sys.argv[0]) + "\"", "", 1)
    sys.exit()

window = tk.Tk()
window.title("Process restart tool")
window.resizable(False, False)
window.configure(padx = 16, pady = 14)

icon = tk.PhotoImage(data = "iVBORw0KGgoAAAANSUhEUgAAAEwAAABMBAMAAAA1uUwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAYUExURQAAAAAaaAA+kgBnwAB41ACR+EzC/5nr/8MyyRkAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAA9SURBVEjH7coxAQAQFEXRLwIRiEAEIhCB1aa+l4LlnvnYH85LiJKylCqty5iyjmwajUaj0Wg0Gu19e87sAnxWiuenyOclAAAAAElFTkSuQmCC")
window.iconphoto(True, icon)

ttk.Label(window, text = "Click one of the following buttons to restart a process").pack(anchor = "w", pady = (0, 14))
ttk.Button(window, text = "Restart explorer.exe", command = lambda: subprocess.call("taskkill /f /im explorer.exe & start explorer", shell = True)).pack(fill = "x")
ttk.Button(window, text = "Restart dwm.exe", command = lambda: subprocess.call("taskkill /f /im dwm.exe", shell = True)).pack(fill = "x", pady = (4, 0))

window.mainloop()