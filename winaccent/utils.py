'''
A winaccent submodule containing functions used internaly.
'''

import winreg

def get_registry_value(hkey, key_path, value_name):
    key = winreg.OpenKey(hkey, key_path, 0, winreg.KEY_READ)
    value, regtype = winreg.QueryValueEx(key, value_name)
    winreg.CloseKey(key)
    
    return value

def get_color_from_registry_rgb(hkey, key_path, value_name, from_):
    list = f"{get_registry_value(hkey, key_path, value_name):08X}"
    color = "#"

    if from_ == "abgr": color = "#" + list[6] + list[7] + list[4] + list[5] + list[2] + list[3]
    elif from_ == "argb": color = "#" + list[2] + list[3] + list[4] + list[5] + list[6] + list[7]

    if list[0] + list[1] + color.replace("#", "") == "00000000": return "0"
    else: return color