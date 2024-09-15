'''
A simple module for getting Windows' accent color. With this module you can get both light and dark mode accent colors.
'''

import sys, time
class UnsupportedPlatformException(Exception): pass

if not sys.platform == "win32" or not sys.getwindowsversion().major == 10: 
    raise UnsupportedPlatformException("This module only works on Windows 10 and later!")
else: import winreg

def get_registry_value(hkey, key_path, value_name):
    key = winreg.OpenKey(hkey, key_path, 0, winreg.KEY_READ)
    value, regtype = winreg.QueryValueEx(key, value_name)
    winreg.CloseKey(key)
    
    return value

def update_accent_colors():
    '''Updates the accent color variables.'''

    global accent_light, accent_dark, accent_normal, accent_dark_3, accent_dark_2, accent_dark_1, accent_light_3, accent_light_2, accent_light_1, accent_dark_mode, accent_light_mode

    accent_palette = get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "AccentPalette")
    accent_palette = " ".join(f'{byte:02X}' for byte in accent_palette)
    accent_palette_list = accent_palette.split(" ")

    # Guidelines: https://learn.microsoft.com/en-us/windows/apps/design/style/color#accent-color-palette
    accent_light_3 = "#" + accent_palette_list[0] + accent_palette_list[1] + accent_palette_list[2]
    accent_light_2 = "#" + accent_palette_list[4] + accent_palette_list[5] + accent_palette_list[6]
    accent_light_1 = "#" + accent_palette_list[8] + accent_palette_list[9] + accent_palette_list[10]
    accent_normal = "#" + accent_palette_list[12] + accent_palette_list[13] + accent_palette_list[14]
    accent_dark_1 = "#" + accent_palette_list[16] + accent_palette_list[17] + accent_palette_list[18]
    accent_dark_2 = "#" + accent_palette_list[20] + accent_palette_list[21] + accent_palette_list[22]
    accent_dark_3 = "#" + accent_palette_list[24] + accent_palette_list[25] + accent_palette_list[26]

    accent_dark = accent_dark_1
    accent_light = accent_light_2

    accent_dark_mode = accent_light
    accent_light_mode = accent_dark

    # Some weird color (possibly a complementary color for the accent color)
    # "#" + accent_palette_list[28] + accent_palette_list[29] + accent_palette_list[30]

def on_accent_changed_listener(callback: callable):
    '''Listens for accent color changes. If the accent color changed, the function
    specified in the `callback` argument will be called.'''

    while True:
        old_value = accent_normal
        update_accent_colors()

        if old_value != accent_normal: callback()
        time.sleep(1)

update_accent_colors()