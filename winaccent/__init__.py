'''
A simple and lightweight Python module for easily retrieving Windows' accent color, including shades, specific window colors such as active/inactive titlebar and window borders and theme. Supports Windows 8.x, 10 and 11 and doesn't require additional dependencies.
'''

import sys, time

if not sys.platform == "win32": 
    raise ImportError("No Windows environment found. This module only works on Windows 8 and later.")
elif sys.getwindowsversion().major == 10: 
    from . import _win_10 as win
elif sys.getwindowsversion().major == 6 and sys.getwindowsversion().minor >= 2:
    from . import _win_8 as win
else:
    raise ImportError("Incompatible Windows version. This module only works on Windows 8 and later.")

# Flags
get_accent_from_dwm: bool = False

# Colors
accent_dark: str
accent_light: str
accent_dark_mode: str
accent_light_mode: str
accent_normal: str
accent_dark_3: str
accent_dark_2: str
accent_dark_1: str
accent_light_3: str
accent_light_2: str
accent_light_1: str
accent_dark_mode: str
accent_light_mode: str
titlebar_active: str
titlebar_inactive: str
window_border: str
accent_menu: str

# Other settings
is_titlebar_colored: bool
apps_use_light_theme: bool
system_uses_light_theme: bool

# Event constants
class event:
    accent_color_changed = 0
    window_chrome_color_changed = 1
    apps_theme_changed = 2
    system_theme_changed = 3


def update_values() -> None: 
    '''Updates the accent color variables.'''
    
    global get_accent_from_dwm

    global accent_dark
    global accent_light
    global accent_dark_mode
    global accent_light_mode
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
    global apps_use_light_theme
    global system_uses_light_theme

    win.get_accent_from_dwm = get_accent_from_dwm
    win.update_values()

    accent_light_3 = win.accent_light_3
    accent_light_2 = win.accent_light_2
    accent_light_1 = win.accent_light_1
    accent_normal = win.accent_normal
    accent_dark_1 = win.accent_dark_1
    accent_dark_2 = win.accent_dark_2
    accent_dark_3 = win.accent_dark_3

    accent_dark = accent_dark_1
    accent_light = accent_light_2
    accent_dark_mode = accent_light
    accent_light_mode = accent_dark

    is_titlebar_colored = win.is_titlebar_colored
    titlebar_active = win.titlebar_active
    titlebar_inactive = win.titlebar_inactive
    window_border = win.window_border

    accent_menu = win.accent_menu

    apps_use_light_theme = win.apps_use_light_theme
    system_uses_light_theme = win.system_uses_light_theme

update_values()


def on_appearance_changed(callback: callable, pass_event: bool = False) -> None:
    '''Listens for appearance settings changes (accent color, system theme, window colors). 
    If one of them changes, the function specified in the `callback` argument will be called.'''

    while True:
        accent_light_1_old = accent_light_1
        accent_light_2_old = accent_light_2
        accent_light_3_old = accent_light_3
        accent_old = accent_normal
        accent_dark_1_old = accent_dark_1
        accent_dark_2_old = accent_dark_2
        accent_dark_3_old = accent_dark_3

        is_titlebar_colored_old = is_titlebar_colored
        titlebar_active_old = titlebar_active
        titlebar_inactive_old = titlebar_inactive
        window_border_old = window_border

        accent_menu_old = accent_menu
        
        apps_use_light_theme_old = apps_use_light_theme
        system_uses_light_theme_old = system_uses_light_theme
        
        update_values()

        if (accent_light_3_old != accent_light_3 or
            accent_light_2_old != accent_light_2 or
            accent_light_1_old != accent_light_1 or
            accent_old != accent_normal or 
            accent_dark_1_old != accent_dark_1 or
            accent_dark_2_old != accent_dark_2 or
            accent_dark_3_old != accent_dark_3 or
            
            accent_menu_old != accent_menu
        ): 
            # Accent color changed
            if pass_event: callback(event = 0)
            else: callback()

        elif (is_titlebar_colored_old != is_titlebar_colored or
              titlebar_active_old != titlebar_active or
              titlebar_inactive_old != titlebar_inactive or
              window_border_old != window_border
        ): 
            # Active/inactive titlebar or window border color changed
            if pass_event: callback(event = 1)
            else: callback()

        elif (apps_use_light_theme_old != apps_use_light_theme): 
            # Apps theme changed
            if pass_event: callback(event = 2)
            else: callback()
        elif (system_uses_light_theme_old != system_uses_light_theme):
            # System theme changed
            if pass_event: callback(event = 3)
            else: callback()

        time.sleep(1)

def hex_to_rgb(hex: str) -> tuple:
    '''Function to convert a HEX color to an RGB tuple if needed.'''

    if hex == None:
        return None
    else:
        if isinstance(hex, str):
            if len(hex) == 7 and hex.startswith("#"): hex = hex.lstrip("#"); print(hex)
            if len(hex) == 6:
                try: red = int(hex[0] + hex[1], base = 16)
                except: raise ValueError("Invalid red value")

                try: green = int(hex[2] + hex[3], base = 16)
                except: raise ValueError("Invalid green value")

                try: blue = int(hex[4] + hex[5], base = 16)
                except: raise ValueError("Invalid blue value")

                return (red, green, blue)
            else:
                raise ValueError("Invalid HEX color")
        else:
            raise ValueError("`hex` must be an instance of str")