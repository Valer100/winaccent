'''
A simple module for getting Windows' accent color. With this module you can get both light and dark mode accent colors.
'''

import winreg, sys, time, typing

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

def manipulate_color(color: str, factor: int, action: typing.Literal["lighten", "darken"]) -> str:
    if not action in ["lighten", "darken"]:
        raise ValueError("Invalid value for the `action` argument. It must be either `lighten` or `darken` (without `)")

    if action == "lighten": factor *= -1

    red = int(color[1] + color[2], base = 16) - factor
    green = int(color[3] + color[4], base = 16) - factor
    blue = int(color[5] + color[6], base = 16) - factor

    if red < 0: red = 0
    if red > 255: red = 255

    if green < 0: green = 0
    if green > 255: green = 255

    if blue < 0: blue = 0
    if blue > 255: blue = 255

    print(red, green, blue)

    red_hex_str = f"{red:x}"
    green_hex_str = f"{green:x}"
    blue_hex_str = f"{blue:x}"

    if len(red_hex_str) == 1: red_hex_str = "0" + red_hex_str
    if len(green_hex_str) == 1: green_hex_str = "0" + green_hex_str
    if len(blue_hex_str) == 1: blue_hex_str = "0" + blue_hex_str

    return "#" + red_hex_str + green_hex_str + blue_hex_str

update_accent_colors()