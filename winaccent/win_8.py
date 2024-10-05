from . import utils
import winreg, sys

# For Windows 8.0

accent_menu_colors = [
    "#252525",
    "#252525",
    "#252525",
    "#252525",
    "#2E1700",
    "#4E0000",
    "#4E0038",
    "#2D004E",
    "#1F0068",
    "#001E4E",
    "#004D60",
    "#004A00",
    "#15992A",
    "#E56C19",
    "#B81B1B",
    "#B81B6C",
    "#691BB8",
    "#1B58B8",
    "#569CE3",
    "#00AAAA",
    "#83BA1F",
    "#D39D09",
    "#E064B7",
    "#696969",
    "#696969"
]

accent_normal_colors = [
    "#F4B300",
    "#78BA00",
    "#2673EC",
    "#AE113D",
    "#632F00",
    "#B01E00",
    "#C1004F",
    "#7200AC",
    "#4617B4",
    "#006AC1",
    "#008287",
    "#199900",
    "#00C13F",
    "#FF981D",
    "#FF2E12",
    "#FF1D77",
    "#AA40FF",
    "#1FAEFF",
    "#56C5FF",
    "#00D8CC",
    "#91D100",
    "#E1B700",
    "#FF76BC",
    "#00A4A4",
    "#FF7D23"
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

    if sys.getwindowsversion().minor >= 2:
        try: color_scheme = utils.get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "ColorSet_Version3")
        except: color_scheme = 8

        if color_scheme > 24: color_scheme = 8

        accent_normal = accent_normal_colors[color_scheme]
        accent_menu = accent_menu_colors[color_scheme]
    else:
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