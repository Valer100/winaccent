'''
A simple module for getting Windows' accent color. With this module you can get both light and dark mode accent colors.
'''

import sys, time
class UnsupportedPlatformException(Exception): pass

if not sys.platform == "win32" or not sys.getwindowsversion().major == 10: 
    raise UnsupportedPlatformException("This module only works on Windows 10 and later!")
else: 
    from . import utils
    import winreg

def update_accent_colors():
    '''Updates the accent color variables.'''

    global accent_light, accent_dark, accent_normal, accent_dark_3, accent_dark_2, accent_dark_1, accent_light_3, accent_light_2, accent_light_1, accent_dark_mode, accent_light_mode, titlebar_active, titlebar_inactive, is_titlebar_colored, window_border, accent_menu

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
    
    try: accent_menu = utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "AccentColorMenu", "abgr")
    except: accent_menu = accent_normal

    accent_dark = accent_dark_1
    accent_light = accent_light_2

    accent_dark_mode = accent_light
    accent_light_mode = accent_dark

    titlebar_active = utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "AccentColor", "abgr")
    
    try: titlebar_inactive = utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "AccentColorInactive", "abgr")
    except: titlebar_inactive = None

    window_border = utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "ColorizationColor", "argb")

    # Replicate Windows' behavior if titlebar_active, titlebar_inactive and window_border are set to 0
    if titlebar_active == "0": titlebar_active = accent_menu
    if titlebar_inactive == "0": titlebar_inactive = accent_menu
    if accent_menu == "0": accent_menu = accent_normal
    if window_border == "0": window_border = "#000000"

    is_titlebar_colored = utils.get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "ColorPrevalence")

def on_accent_changed_listener(callback: callable):
    '''Listens for accent color changes. If the accent color changed, the function
    specified in the `callback` argument will be called.'''

    while True:
        accent_old = accent_normal
        is_titlebar_colored_old = is_titlebar_colored
        titlebar_active_old = titlebar_active
        titlebar_inactive_old = titlebar_inactive
        accent_menu_old = accent_menu
        window_border_old = window_border
        update_accent_colors()

        if (accent_old != accent_normal or 
            is_titlebar_colored_old != is_titlebar_colored or
            titlebar_active_old != titlebar_active or
            titlebar_inactive_old != titlebar_inactive or
            window_border_old != window_border or
            accent_menu_old != accent_menu
        ): callback()
        
        time.sleep(1)

update_accent_colors()