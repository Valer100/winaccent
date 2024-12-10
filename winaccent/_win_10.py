'''
A winaccent submodule that contains code for Windows 10 and 11.
'''

from . import _utils
import winreg, sys

def update_values():
    global get_accent_from_dwm
    global dark_mode_titlebar

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
    
    global apps_use_light_theme
    global system_uses_light_theme

    # Retrieve accent color palette
    try:
        accent_palette = _utils.get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "AccentPalette", winreg.REG_BINARY)
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
        # If it can't be retrieved, use fallback values, depending on the Windows version
        if sys.getwindowsversion().major == 10 and sys.getwindowsversion().build >= 22000:
            # Windows 11
            accent_light_3 = "#99EBFF"
            accent_light_2 = "#4CC2FF"
            accent_light_1 = "#0091F8"
            accent_normal = "#0078D4"
            accent_dark_1 = "#0067C0"
            accent_dark_2 = "#003E92"
            accent_dark_3 = "#001A68"
        elif sys.getwindowsversion().major == 10:
            # Windows 10
            accent_light_3 = "#A6D8FF"
            accent_light_2 = "#76B9ED"
            accent_light_1 = "#429CE3"
            accent_normal = "#0078D7"
            accent_dark_1 = "#005A9E"
            accent_dark_2 = "#004275"
            accent_dark_3 = "#002642"

    # Retrieve accent_menu color
    try: accent_menu = _utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "AccentColorMenu", "abgr")
    except: accent_menu = accent_normal

    # Retrieve active titlebar color (for colored titlebars)
    try: titlebar_active = _utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "AccentColor", "abgr")
    except: titlebar_active = accent_menu

    # Retrieve inactive titlebar color (for colored titlebars)
    try: 
        titlebar_inactive = _utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "AccentColorInactive", "abgr")
        titlebar_inactive_custom_color = True
    except: 
        # If it can't be retrieved, use hardcoded values depending on the Windows version
        # This means that the color isn't set in the registry or it's invalid

        if sys.getwindowsversion().major == 10 and sys.getwindowsversion().build < 22621:
            # Windows 10
            if dark_mode_titlebar:
                titlebar_inactive = "#2B2B2B"
                titlebar_inactive_text = "#808080"
            else:
                titlebar_inactive = "#FFFFFF"
                titlebar_inactive_text = "#999999"
        else:
            # Windows 11
            if dark_mode_titlebar:
                titlebar_inactive = "#202020"
                titlebar_inactive_text = "#797979"
            else:
                titlebar_inactive = "#F3F3F3"
                titlebar_inactive_text = "#929292"

        titlebar_inactive_custom_color = False

    # Retrieve active window border color intensity (useful for retrieving the atcual window border color on Windows 10)
    try: window_border_active_intensity = _utils.get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "ColorizationColorBalance")
    except: window_border_active_intensity = 0

    if sys.getwindowsversion().build >= 22000: 
        # On Windows 11 the active window border color is the same as the active titlebar color
        window_border_active = titlebar_active
    else:
        # On Windows 10 it isn't the same as the active titlebar color
        # The one stored in the registry needs to be blend with "#D9D9D9" with the intensity we retrieved earlier
        try: 
            window_border_max_intensity = _utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "ColorizationColor", "argb")
            window_border_active = _utils.blend_colors(window_border_max_intensity, "#D9D9D9", window_border_active_intensity)
        except: 
            window_border_active = "#9E9E9E"

    # Replicate Windows' behavior if titlebar_active, titlebar_inactive and window_border are set to 0
    if titlebar_active == "0": titlebar_active = accent_menu
    if titlebar_inactive == "0": titlebar_inactive = accent_menu
    if accent_menu == "0": accent_menu = accent_normal
    if window_border_active == "0": window_border = "#000000"

    # Retrieve active titlebar text color (for colored titlebars)
    titlebar_active_text = "#FFFFFF" if _utils.white_text_on_color(titlebar_active) else "#000000"
    
    # Retrieve inactive titlebar text color (for colored titlebars)
    titlebar_inactive_text_no_blend = "#FFFFFF" if _utils.white_text_on_color(titlebar_inactive) else "#000000"
    titlebar_inactive_text = _utils.blend_colors(titlebar_inactive_text_no_blend, titlebar_inactive, 40)

    # If `get_accent_from_dwm` flag is active, generate an alternative accent color pallete based on the active titlebar color
    if get_accent_from_dwm and accent_normal != titlebar_active:
        accent_normal = titlebar_active
        accent_palette = _utils.generate_color_palette(accent_normal)

        accent_light_3 = accent_palette[0]
        accent_light_2 = accent_palette[1]
        accent_light_1 = accent_palette[2]
        accent_dark_1 = accent_palette[3]
        accent_dark_2 = accent_palette[4]
        accent_dark_3 = accent_palette[5]

    # Retrieve the value of the "Show accent color on title bars and window borders" setting
    try:
        is_titlebar_colored = _utils.get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "ColorPrevalence")

        if is_titlebar_colored > 0: is_titlebar_colored = True
        else: is_titlebar_colored = False
    except:
        is_titlebar_colored = False

    # Hardcode some colors if the titlebars aren't colored
    if not is_titlebar_colored:
        if sys.getwindowsversion().major == 10 and sys.getwindowsversion().build < 22621:
            if dark_mode_titlebar:
                titlebar_active = "#000000"
                titlebar_active_text = "#FFFFFF"
                titlebar_inactive = "#2B2B2B"
                titlebar_inactive_text = "#808080"
                window_border_active = "#262626"
            else:
                titlebar_active = "#FFFFFF"
                titlebar_active_text = "#000000"
                titlebar_inactive = "#FFFFFF"
                titlebar_inactive_text = "#999999"
                window_border_active = "#707070"
        else:
            if dark_mode_titlebar:
                titlebar_active = "#202020"
                titlebar_active_text = "#FFFFFF"
                titlebar_inactive = "#202020"
                titlebar_inactive_text = "#797979"
                window_border_active = "#404040"
            else:
                titlebar_active = "#F3F3F3"
                titlebar_active_text = "#000000"
                titlebar_inactive = "#F3F3F3"
                titlebar_inactive_text = "#929292"
                window_border_active = "#404040"

    # More color hardcoding
    if sys.getwindowsversion().major == 10 and sys.getwindowsversion().build < 22621:
        if dark_mode_titlebar: window_border_inactive = "#262626"
        else: window_border_inactive = "#AAAAAA"
    else:
        if is_titlebar_colored and titlebar_inactive_custom_color:
            # On Windows 11 inactive window border color is the same as the inactive titlebar color
            window_border_inactive = titlebar_inactive
        else:
            if dark_mode_titlebar: window_border_inactive = "#404040"
            else: window_border_inactive = "#404040"

    # Retrieve apps' theme
    try:
        apps_use_light_theme = _utils.get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize", "AppsUseLightTheme")

        if apps_use_light_theme > 0: apps_use_light_theme = True
        else: apps_use_light_theme = False
    except:
        apps_use_light_theme = True

    # Retrieve system's theme
    try:
        system_uses_light_theme = _utils.get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize", "SystemUsesLightTheme")

        if system_uses_light_theme == 0: system_uses_light_theme = False
        else: system_uses_light_theme = True
    except:
        system_uses_light_theme = False