'''
A winaccent submodule containing functions used internaly.
'''

import winreg

def get_registry_value(hkey, key_path, value_name):
    key = winreg.OpenKey(hkey, key_path, 0, winreg.KEY_READ)
    value, regtype = winreg.QueryValueEx(key, value_name)
    winreg.CloseKey(key)
    
    return value

def get_color_from_registry_rgb(hkey, key_path, value_name, from_) -> str:
    list = f"{get_registry_value(hkey, key_path, value_name):08X}"
    color = "#"

    if from_ == "abgr": color = "#" + list[6] + list[7] + list[4] + list[5] + list[2] + list[3]
    elif from_ == "argb": color = "#" + list[2] + list[3] + list[4] + list[5] + list[6] + list[7]

    if list[0] + list[1] + color.replace("#", "") == "00000000": return "0"
    else: return color

def blend_colors(color_1: str, color_2: str, intensity: int) -> str:
    intensity = intensity * 255 / 100

    color_1_red = int(color_1[1] + color_1[2], base = 16)
    color_1_green = int(color_1[3] + color_1[4], base = 16)
    color_1_blue = int(color_1[5] + color_1[6], base = 16)

    color_2_red = int(color_2[1] + color_2[2], base = 16)
    color_2_green = int(color_2[3] + color_2[4], base = 16)
    color_2_blue = int(color_2[5] + color_2[6], base = 16)

    red = (((color_1_red * intensity)) + (color_2_red * (255 - intensity))) / 255
    green = (((color_1_green * intensity)) + (color_2_green * (255 - intensity))) / 255
    blue = (((color_1_blue * intensity)) + (color_2_blue * (255 - intensity))) / 255

    return f"#{round(red):02X}{round(green):02X}{round(blue):02X}"