'''
A simple module for getting Windows' accent color. With this module you can get both light and dark mode accent colors.
'''

import sys, time
class UnsupportedPlatformException(Exception): pass

if not sys.platform == "win32": 
    raise UnsupportedPlatformException("This module only works on Windows 8 and later!")
elif sys.getwindowsversion().major == 10: 
    from . import win_10_11 as win
elif sys.getwindowsversion().major == 8:
    from . import win_8 as win
else:
    raise UnsupportedPlatformException("This module only works on Windows 8 and later!")

def update_accent_colors(): 
    global accent_light, accent_dark, accent_normal, accent_dark_3, accent_dark_2, accent_dark_1, accent_light_3, accent_light_2, accent_light_1, accent_dark_mode, accent_light_mode, titlebar_active, titlebar_inactive, is_titlebar_colored, window_border, accent_menu
    win.update_accent_colors()

    accent_light_3 = win.accent_light_3
    accent_light_2 = win.accent_light_2
    accent_light_1 = win.accent_light_1
    accent_normal = win.accent_normal
    accent_dark_1 = win.accent_dark_1
    accent_dark_2 = win.accent_dark_2
    accent_dark_3 = win.accent_dark_3

    is_titlebar_colored = win.is_titlebar_colored
    titlebar_active = win.titlebar_active
    titlebar_inactive = win.titlebar_inactive
    window_border = win.window_border

    accent_menu = win.accent_menu

update_accent_colors()

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