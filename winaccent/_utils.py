'''
A winaccent submodule containing functions used internaly.
'''

import winreg, colorsys
from typing import Any, Literal

def get_registry_value(hkey: int, key_path: str, value_name: str) -> Any :
    key = winreg.OpenKey(hkey, key_path, 0, winreg.KEY_READ)
    value, regtype = winreg.QueryValueEx(key, value_name)
    winreg.CloseKey(key)
    
    return value

def get_color_from_registry_rgb(hkey: int, key_path: str, value_name: str, from_: Literal["abgr", "argb"]) -> str:
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

def increase_saturation(color: str, factor: float) -> str:
    red = int(color[1] + color[2], base = 16) / 255
    green = int(color[3] + color[4], base = 16) / 255
    blue = int(color[5] + color[6], base = 16) / 255
    
    hue, lightness, saturation = colorsys.rgb_to_hls(red, green, blue)
    saturation = min(1, saturation * factor)
    red, green, blue = colorsys.hls_to_rgb(hue, lightness, saturation)
    
    return f"#{round(red * 255):02X}{round(green * 255):02X}{round(blue * 255):02X}"

def white_text_on_color(color: str) -> bool:
    red = int(color[1] + color[2], base = 16)
    green = int(color[3] + color[4], base = 16)
    blue = int(color[5] + color[6], base = 16)

    return (5 * green + 2 * red + blue) <= 8 * 128

def generate_color_palette(color: str) -> list:
    return [
        increase_saturation(blend_colors("#FFFFFF", color, 75), 2),
        increase_saturation(blend_colors("#FFFFFF", color, 50), 2),
        increase_saturation(blend_colors("#FFFFFF", color, 25), 2),
        increase_saturation(blend_colors("#000000", color, 25), 2),
        increase_saturation(blend_colors("#000000", color, 50), 2),
        increase_saturation(blend_colors("#000000", color, 75), 2),
    ]