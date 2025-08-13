'''
A winaccent submodule that contains code for Windows Vista and 7.
'''

from . import _utils
import winreg, sys


def update_values():
    global os_has_full_support

    global get_accent_from_dwm
    global dark_mode_window

    global accent_menu
    
    global accent_light_3
    global accent_light_2
    global accent_light_1
    global accent_normal
    global accent_dark_3
    global accent_dark_2
    global accent_dark_1

    global is_titlebar_colored
    global titlebar_active
    global titlebar_active_text
    global titlebar_inactive
    global titlebar_inactive_text
    global window_border_active
    global window_border_inactive
    
    global is_start_menu_colored
    global start_menu

    global is_taskbar_colored
    global taskbar
    global is_taskbar_center_aligned
    global is_taskbar_auto_hiding

    global transparency_effects_enabled
    global apps_use_light_theme
    global system_uses_light_theme


    # Limited support
    os_has_full_support = False


    # Retrieve accent color from DWM
    try:
        accent_normal = _utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "ColorizationColor", "argb")
    except:
        if sys.getwindowsversion() == 0: accent_normal = "#409EFE"
        else: accent_normal = "#74B8FC"

    if accent_normal == "0": accent_normal = "#000000"
    accent_menu = accent_normal


    # Generate a color palette for the accent color
    accent_palette = _utils.generate_color_palette(accent_normal)

    accent_light_3 = accent_palette[0]
    accent_light_2 = accent_palette[1]
    accent_light_1 = accent_palette[2]
    accent_dark_1 = accent_palette[3]
    accent_dark_2 = accent_palette[4]
    accent_dark_3 = accent_palette[5]


    # Retrieve transparency effects setting
    try:
        transparency_effects_enabled = _utils.get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "ColorizationOpaqueBlend")

        if transparency_effects_enabled > 0: transparency_effects_enabled = False
        else: transparency_effects_enabled = True
    except:
        transparency_effects_enabled = True


    # Retrieve taskbar autohide setting
    try:
        stuckrects3_settings = _utils.get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\StuckRects3", "Settings", winreg.REG_BINARY)
        stuckrects3_settings = " ".join(f'{byte:02X}' for byte in stuckrects3_settings)
        stuckrects3_settings_list = stuckrects3_settings.split(" ")

        is_taskbar_auto_hiding = stuckrects3_settings_list[8][1]

        if is_taskbar_auto_hiding >= 3: is_taskbar_auto_hiding = True
        else: is_taskbar_auto_hiding = False
    except:
        is_taskbar_auto_hiding = False


    # Unsupported values
    titlebar_active = None
    titlebar_active_text = None
    titlebar_inactive = None
    titlebar_inactive_text = None
    window_border_active = None
    window_border_inactive = None
    start_menu = None
    taskbar = None


    # Hardcode these values to `True`
    is_titlebar_colored = True
    is_start_menu_colored = True
    is_taskbar_colored = True
    apps_use_light_theme = True
    system_uses_light_theme = True


    # Hardcode these values to `False`
    is_taskbar_center_aligned = False