'''
A winaccent submodule that contains code for Windows 10 and 11.
'''

from . import utils
import winreg, sys

def update_accent_colors():
    '''Updates the accent color variables.'''

    global accent_normal
    global accent_dark_3
    global accent_dark_2
    global accent_dark_1
    global accent_light_3
    global accent_light_2
    global accent_light_1
    global titlebar_active
    global titlebar_inactive
    global is_titlebar_colored
    global window_border
    global accent_menu

    try:
        accent_palette = utils.get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "AccentPalette")
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
    except:
        if sys.getwindowsversion().major == 10 and sys.getwindowsversion().build >= 22000:
            accent_light_3 = "#99EBFF"
            accent_light_2 = "#4CC2FF"
            accent_light_1 = "#0091F8"
            accent_normal = "#0078D4"
            accent_dark_1 = "#0067C0"
            accent_dark_2 = "#003E92"
            accent_dark_3 = "#001A68"
        elif sys.getwindowsversion().major == 10:
            accent_light_3 = "#A6D8FF"
            accent_light_2 = "#76B9ED"
            accent_light_1 = "#429CE3"
            accent_normal = "#0078D7"
            accent_dark_1 = "#005A9E"
            accent_dark_2 = "#004275"
            accent_dark_3 = "#002642"

    try: accent_menu = utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "AccentColorMenu", "abgr")
    except: accent_menu = accent_normal

    try: titlebar_active = utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "AccentColor", "abgr")
    except: titlebar_active = accent_menu

    try: titlebar_inactive = utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "AccentColorInactive", "abgr")
    except: titlebar_inactive = None

    try:
        window_border_intensity = utils.get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "ColorizationColorBalance")
        window_border_intensity = 255 * window_border_intensity / 100
    except:
        window_border_intensity = 0

    if sys.getwindowsversion().build >= 22000: 
        window_border = titlebar_active
    else:
        try: 
            window_border_max_intensity = utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "ColorizationColor", "argb")
            window_border = utils.blend_colors(window_border_max_intensity, "#D9D9D9", window_border_intensity)
        except: 
            window_border = "#9E9E9E"

    # Replicate Windows' behavior if titlebar_active, titlebar_inactive and window_border are set to 0
    if titlebar_active == "0": titlebar_active = accent_menu
    if titlebar_inactive == "0": titlebar_inactive = accent_menu
    if accent_menu == "0": accent_menu = accent_normal
    if window_border == "0": window_border = "#000000"

    try:
        is_titlebar_colored = utils.get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "ColorPrevalence")

        if is_titlebar_colored > 0: is_titlebar_colored = True
        else: is_titlebar_colored = False
    except:
        is_titlebar_colored = False