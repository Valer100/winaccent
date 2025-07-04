'''
A winaccent submodule that contains code for Windows 8 and 8.1.
'''

from . import _utils
import winreg, sys

# IMPORTANT!
# `accent_menu` represents here the Start menu color

# Windows 8.0 color schemes' colors
accent_menu_colors = [
    "#252525", "#252525", "#252525", "#252525", "#2E1700",
    "#4E0000", "#4E0038", "#2D004E", "#1F0068", "#001E4E",
    "#004D60", "#004A00", "#15992A", "#E56C19", "#B81B1B",
    "#B81B6C", "#691BB8", "#1B58B8", "#569CE3", "#00AAAA",
    "#83BA1F", "#D39D09", "#E064B7", "#696969", "#696969"
]

accent_normal_colors = [
    "#F4B300", "#78BA00", "#2673EC", "#AE113D", "#632F00",
    "#B01E00", "#C1004F", "#7200AC", "#4617B4", "#006AC1",
    "#008287", "#199900", "#00C13F", "#FF981D", "#FF2E12",
    "#FF1D77", "#AA40FF", "#1FAEFF", "#56C5FF", "#00D8CC",
    "#91D100", "#E1B700", "#FF76BC", "#00A4A4", "#FF7D23"
]

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
    global is_taskbar_colored
    global start_menu
    global taskbar

    global transparency_effects_enabled
    global apps_use_light_theme
    global system_uses_light_theme


    # Full support
    os_has_full_support = True


    if sys.getwindowsversion().minor == 2:
        # Windows 8.0

        try:
            # Try retrieving the user's color scheme number
            color_scheme = _utils.get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "ColorSet_Version3")
        except: 
            try: 
                # If retrieving the user's color scheme number fails, try retrieving the machine-wide color scheme number
                color_scheme = _utils.get_registry_value(winreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "DefaultColorSet")
            except: 
                # If retrieving the machine-wide color scheme number also fails, use the fallback number (8)
                color_scheme = 8

        # If the color scheme number is greater than 24, use the fallback number (8)
        if color_scheme > 24: color_scheme = 8

        # Retrieve the accent_normal and accent_menu colors from the current color scheme
        accent_normal = accent_normal_colors[color_scheme]
        accent_menu = accent_menu_colors[color_scheme]

    elif sys.getwindowsversion().minor == 3:
        # Windows 8.1

        # Try retrieving the accent colors set through Group Policy
        try: 
            accent_normal = _utils.get_registry_value(winreg.HKEY_LOCAL_MACHINE, "Software\\Policies\\Microsoft\\Windows\\Personalization", "PersonalColors_Accent") 
            accent_menu = _utils.get_registry_value(winreg.HKEY_LOCAL_MACHINE, "Software\\Policies\\Microsoft\\Windows\\Personalization", "PersonalColors_Background")

            # Check if the colors are valid
            # If not, raise an exception, since things go weird
            
            if len(accent_normal) != 7 or len(accent_menu) != 7:
                raise ValueError("Invalid `accent_normal` or `accent_menu` color")

            try:
                accent_normal_test = int(accent_normal[1] + accent_normal[2], base = 16) + int(accent_normal[3] + accent_normal[4], base = 16) + int(accent_normal[5] + accent_normal[6], base = 16)
                accent_menu_test = int(accent_menu[1] + accent_menu[2], base = 16) + int(accent_menu[3] + accent_menu[4], base = 16) + int(accent_menu[5] + accent_menu[6], base = 16)
            except:
                raise ValueError("Invalid `accent_normal` or `accent_menu` color")
        except:
            # If that fails, try retrieving the user's accent colors
            try: 
                accent_normal = _utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "AccentColor", "abgr")
                accent_menu = _utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "StartColor", "abgr")
            except: 
                # If that also fails, try retrieving the machine-wide ones
                try: 
                    accent_normal = _utils.get_color_from_registry_rgb(winreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "DefaultAccentColor", "abgr") 
                    accent_menu = _utils.get_color_from_registry_rgb(winreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "DefaultStartColor", "abgr")
                except: 
                    # If that also fails, use fallback colors
                    accent_normal = "#4617B4"
                    accent_menu = "#180052"

        if accent_normal == "0": accent_normal = "#000000"
        if accent_menu == "0": accent_menu = "#000000"

    start_menu = accent_menu


    # Generate a color palette for the accent color (Windows 8.x doesn't generate one automatically)
    accent_palette = _utils.generate_color_palette(accent_normal)

    accent_light_3 = accent_palette[0]
    accent_light_2 = accent_palette[1]
    accent_light_1 = accent_palette[2]
    accent_dark_1 = accent_palette[3]
    accent_dark_2 = accent_palette[4]
    accent_dark_3 = accent_palette[5]


    # Retrieve active titlebar color intensity (useful for retrieving the actual active titlebar color)
    try: titlebar_active_intensity = _utils.get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "ColorizationColorBalance")
    except: titlebar_active_intensity = 0


    # Retrieve the actual active titlebar color
    # You have to get the active titlebar color with max intensity and then blend it with "#D9D9D9" with the intensity we retrieved previously
    try:
        titlebar_active_max_intensity = _utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "ColorizationColor", "argb")
        titlebar_active = _utils.blend_colors(titlebar_active_max_intensity, "#D9D9D9", titlebar_active_intensity)
    except:
        titlebar_active_max_intensity = "#9E9E9E"
        titlebar_active = "#9E9E9E"


    # The taskbar color is the same as the active titlebar color
    taskbar = titlebar_active


    # Hardcode active titlebar text color
    titlebar_active_text = "#282828"


    # If `get_accent_from_dwm` flag is active, generate an alternative accent color pallete based on the active titlebar color
    if get_accent_from_dwm:
        accent_normal = titlebar_active_max_intensity
        accent_palette = _utils.generate_color_palette(accent_normal)

        accent_light_3 = accent_palette[0]
        accent_light_2 = accent_palette[1]
        accent_light_1 = accent_palette[2]
        accent_dark_1 = accent_palette[3]
        accent_dark_2 = accent_palette[4]
        accent_dark_3 = accent_palette[5]


    # Hardcode inactive titlebar color and text color
    titlebar_inactive = "#EBEBEB"
    titlebar_inactive_text = "#282828"


    # Set active window border color to the active titlebar color
    window_border_active = titlebar_active


    # Hardcode inactive window border color
    window_border_inactive = "#EBEBEB"


    # Hardcode these values to `True`
    is_titlebar_colored = True
    is_start_menu_colored = True
    is_taskbar_colored = True
    transparency_effects_enabled = True
    apps_use_light_theme = True
    system_uses_light_theme = True