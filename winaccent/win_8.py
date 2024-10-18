'''
A winaccent submodule that contains code for Windows 8 and 8.1.
'''

from . import utils
import winreg, sys

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

    if sys.getwindowsversion().minor == 2:
        try: color_scheme = utils.get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "ColorSet_Version3")
        except: 
            try: color_scheme = utils.get_registry_value(winreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "DefaultColorSet")
            except: color_scheme = 8

        if color_scheme > 24: color_scheme = 8

        accent_normal = accent_normal_colors[color_scheme]
        accent_menu = accent_menu_colors[color_scheme]
    elif sys.getwindowsversion().minor == 3:
        try: 
            accent_normal = utils.get_registry_value(winreg.HKEY_LOCAL_MACHINE, "Software\\Policies\\Microsoft\\Windows\\Personalization", "PersonalColors_Accent") 
            accent_menu = utils.get_registry_value(winreg.HKEY_LOCAL_MACHINE, "Software\\Policies\\Microsoft\\Windows\\Personalization", "PersonalColors_Background")

            if len(accent_normal) != 7 or len(accent_menu) != 7:
                raise ValueError("Invalid `accent_normal` or `accent_menu` color")

            try:
                accent_normal_test = int(accent_normal[1] + accent_normal[2], base = 16) + int(accent_normal[3] + accent_normal[4], base = 16) + int(accent_normal[5] + accent_normal[6], base = 16)
                accent_menu_test = int(accent_menu[1] + accent_menu[2], base = 16) + int(accent_menu[3] + accent_menu[4], base = 16) + int(accent_menu[5] + accent_menu[6], base = 16)
            except:
                raise ValueError("Invalid `accent_normal` or `accent_menu` color")
        except:
            try: 
                accent_normal = utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "AccentColor", "abgr")
                accent_menu = utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "StartColor", "abgr")
            except: 
                try: 
                    accent_normal = utils.get_color_from_registry_rgb(winreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "DefaultAccentColor", "abgr") 
                    accent_menu = utils.get_color_from_registry_rgb(winreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "DefaultStartColor", "abgr")
                except: 
                    accent_normal = "#4617B4"
                    accent_menu = "#180052"

        if not (utils.get_contrast_ratio_with_white(accent_normal) >= 2 or utils.get_contrast_ratio_with_white(accent_menu) >= 2):
            # One of the accent colors doesn't meet the contrast ratio of 2:1 with white text
            # If they do not meet that contrast ratio, they will be set to the default values

            accent_normal = "#4617B4"
            accent_menu = "#180052"

    # Generate accent palette
    accent_light_3 = utils.blend_colors("#FFFFFF", accent_normal, 255 * 75 / 100)
    accent_light_2 = utils.blend_colors("#FFFFFF", accent_normal, 255 * 50 / 100)
    accent_light_1 = utils.blend_colors("#FFFFFF", accent_normal, 255 * 25 / 100)
    accent_dark_1 = utils.blend_colors("#000000", accent_normal, 255 * 25 / 100)
    accent_dark_2 = utils.blend_colors("#000000", accent_normal, 255 * 50 / 100)
    accent_dark_3 = utils.blend_colors("#000000", accent_normal, 255 * 75 / 100)

    try:
        titlebar_active_intensity = utils.get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "ColorizationColorBalance")
        titlebar_active_intensity = 255 * titlebar_active_intensity / 100
    except:
        titlebar_active_intensity = 0

    try:
        titlebar_active_max_intensity = utils.get_color_from_registry_rgb(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\DWM", "ColorizationColor", "argb")
        titlebar_active = utils.blend_colors(titlebar_active_max_intensity, "#D9D9D9", titlebar_active_intensity)
    except:
        titlebar_active = "#9E9E9E"

    titlebar_inactive = "#EBEBEB"
    window_border = titlebar_active

    is_titlebar_colored = True