from . import utils
import winreg

def update_accent_colors():
    '''Updates the accent color variables.'''

    global accent_normal
    global accent_dark_3
    global accent_dark_2
    global accent_dark_1
    global accent_light_3
    global accent_light_2
    global accent_light_1
    global accent_dark_mode
    global accent_light_mode
    global titlebar_active
    global titlebar_inactive
    global is_titlebar_colored
    global window_border
    global accent_menu
    global is_accent_palette_supported
    
    accent_light_3 = None
    accent_light_2 = None
    accent_light_1 = None
    accent_dark_1 = None
    accent_dark_2 = None
    accent_dark_3 = None
    
    accent_normal = utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "AccentColor", "abgr")
    accent_menu = utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "StartColor", "abgr")
    
    titlebar_active_intensity = utils.get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "ColorizationColorBalance")
    titlebar_active_intensity = 255 * titlebar_active_intensity / 100

    titlebar_active_max_intensity = utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "ColorizationColor", "argb")
    titlebar_active = utils.blend_colors(titlebar_active_max_intensity, "#D9D9D9", titlebar_active_intensity)

    titlebar_inactive = "#EBEBEB"
    window_border = titlebar_active

    is_titlebar_colored = True
    is_accent_palette_supported = False