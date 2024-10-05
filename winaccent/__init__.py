'''
A simple module for getting Windows' accent color. With this module you can get both light and dark mode accent colors.
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
is_accent_palette_supported: bool

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
    global is_accent_palette_supported

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
    is_accent_palette_supported = win.is_accent_palette_supported

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