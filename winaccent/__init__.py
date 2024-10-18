'''
A simple and lightweight Python module for getting Windows' accent color, a shade of it or a specific window color (active/inactive titlebar color, window borders color).
'''

import sys, time

if not sys.platform == "win32": 
    raise ImportError("No Windows environment found. This module only works on Windows 8 and later.")
elif sys.getwindowsversion().major == 10: 
    from . import win_10 as win
elif sys.getwindowsversion().major == 6 and sys.getwindowsversion().minor >= 2:
    from . import win_8 as win
else:
    raise ImportError("Incompatible Windows version. This module only works on Windows 8 and later.")

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
is_titlebar_colored: bool

def update_accent_colors() -> None: 
    '''Updates the accent color variables.'''
    
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

    win.update_accent_colors()

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

update_accent_colors()

def on_accent_changed_listener(callback: callable) -> None:
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

def hex_to_rgb(hex: str) -> tuple:
    '''
    Function to convert a HEX color to an RGB tuple if needed.
    '''

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