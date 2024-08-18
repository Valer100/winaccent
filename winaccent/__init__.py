'''
A simple module for getting Windows' accent color. With this module you can get both light and dark mode accent colors.
'''

import winreg, sys, time

if not sys.platform == "win32" or  not sys.getwindowsversion().major == 10: 
    raise Exception("This module only works on Windows 10 and later!")

def get_registry_value(hkey, key_path, value_name):
    key = winreg.OpenKey(hkey, key_path, 0, winreg.KEY_READ)
    value, regtype = winreg.QueryValueEx(key, value_name)
    winreg.CloseKey(key)
    
    return value

def update_accent_colors():
    global accent_light, accent_dark, accent_normal

    accent_palette = get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "AccentPalette")
    accent_palette = " ".join(f'{byte:02X}' for byte in accent_palette)
    accent_palette_list = accent_palette.split(" ")

    accent_light = "#" + accent_palette_list[16] + accent_palette_list[17] + accent_palette_list[18]
    accent_dark = "#" + accent_palette_list[4] + accent_palette_list[5] + accent_palette_list[6]

    dwm = "Software\\Microsoft\\Windows\\DWM"
    accent_normal = f"#{get_registry_value(winreg.HKEY_CURRENT_USER, f'{dwm}', 'ColorizationAfterglow'): X}".replace("# C4", "#")

def on_accent_changed_listener(callback):
    while True:
        old_value = accent_normal
        update_accent_colors()

        if old_value != accent_normal: callback()
        
        time.sleep(1)

update_accent_colors()