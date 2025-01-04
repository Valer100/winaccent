<div align="center">
    <img width="700" src="https://github.com/Valer100/winaccent/blob/main/assets/hero.png?raw=true">
</div>

# winaccent
[![PyPI](https://img.shields.io/pypi/v/winaccent)](https://pypi.org/project/winaccent/)
[![Python](https://img.shields.io/badge/python-3.6+-blue)]()
[![Windows](https://img.shields.io/badge/windows-8.0+-blue)]()
[![Format](https://img.shields.io/pypi/format/winaccent)](https://pypi.org/project/winaccent/)
[![Downloads](https://img.shields.io/pepy/dt/winaccent)](https://pypi.org/project/winaccent/)
[![Stars](https://img.shields.io/github/stars/Valer100/winaccent?style=flat&color=yellow)](https://github.com/Valer100/winaccent/stargazers)
[![Contributors](https://img.shields.io/github/contributors/Valer100/winaccent)](https://github.com/Valer100/winaccent/graphs/contributors)
[![Last commit](https://img.shields.io/github/last-commit/Valer100/winaccent)](https://github.com/Valer100/winaccent/commits/main)
[![Commits since latest release](https://img.shields.io/github/commits-since/Valer100/winaccent/latest)](https://github.com/Valer100/winaccent/commits/main)
[![License](https://img.shields.io/github/license/Valer100/winaccent)](https://github.com/Valer100/winaccent/blob/main/LICENSE)

A simple and lightweight Python module for easily retrieving Windows' accent color, including shades, specific window chrome colors such as active/inactive titlebar and window borders and theme. Supports Windows 8.x, 10 and 11 and doesn't require additional dependencies.

## 📦 Installation
Run this command in your terminal:

```
pip install winaccent
```

To update the module, run this command:

```
pip install --upgrade winaccent
```

## 📝 Requirements
- Windows 8.0 or newer
- Python 3.6 or newer

## 📜 Documentation

> [!IMPORTANT]
> This is a Windows-only module. Trying to import this module on a OS other than Windows or a Windows version older than 8.0 will raise an `ImportError` exception. When using this module in cross-platform applications, make sure you only import and use winaccent on Windows systems to avoid errors. Here's an example:

```python
import sys

if sys.platform == "win32":
    import winaccent
    print(winaccent.accent_normal)
```

If you're using a Python version that supports Windows versions older than 8.0 (Python 3.8 and older), use the following example:

<details>
    <summary>Show the code</summary>

```python
import sys

if sys.platform == "win32":
    # Get Windows version (major.minor)
    version = sys.getwindowsversion()
    current_version = float(f"{version.major}.{version.minor}")

    # Check if the Windows version is greater than or equal to 6.2 (Windows 8)
    # Windows 8.1 will return 6.3 and Windows 10 and 11 will return 10.0
    if current_version >= 6.2:
        import winaccent
        print(winaccent.accent_normal)
```
</details>

---

### Get a specific accent color

> [!NOTE]
> The color values and previews shown here are for Windows 11's default accent color (blue). If you have a different accent color, you'll get the color values based on your accent color.

For simplicity, you can get a specific accent color from one of the following variables:

| Variable | Color |
|----------|:------:
| **accent_dark_mode**<br>(or **accent_light**) | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark.png?raw=true"><br>#4CC2FF |
| **accent_normal** | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_normal.png?raw=true"><br>#0078D4 |
| **accent_light_mode**<br>(or **accent_dark**) | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light.png?raw=true"><br>#0067C0 |

If you need a different shade, you can get it from one of these variables:

| Variable | Color | Variable | Color |
|----------|:-----:|----------|:-----:|
| **accent_light_3** | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark_3.png?raw=true"><br>#99EBFF |**accent_dark_1** | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light.png?raw=true"><br>#0067C0 |
| **accent_light_2** | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark.png?raw=true"><br>#4CC2FF | **accent_dark_2** | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light_2.png?raw=true"><br>#003E92 |
| **accent_light_1** | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark_1.png?raw=true"><br>#0091F8 | **accent_dark_3** | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light_3.png?raw=true"><br>#001A68 |
| **accent_normal** | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_normal.png?raw=true"><br>#0078D4 |

You can get the accent color used in lockscreen, UAC (Windows 10), welcome screen and start menu (Windows 8.x) and other elements using `accent_menu` variable (usually it's the same color as `accent_normal`, but can be modified in the registry).

> [!WARNING]
> The variables will return the colors in HEX color strings (e.g. `#RRGGBB`). If you need an RGB tuple instead of a HEX color string, use the `hex_to_rgb()` function. More information is provided in the [Convert HEX color string to RGB tuple](#convert-hex-color-string-to-rgb-tuple) section.

Example:

```python
import winaccent

print(winaccent.accent_light_mode) # Prints the light mode accent color
```

You may want to take a look at Microsoft's accent color guidelines. You can do that [here](https://learn.microsoft.com/en-us/windows/apps/design/style/color#accent-color-palette).

---

### Get a specific window chrome color
You can use one of these variables:

| Variable | Description |
|:---------|:------------|
| titlebar_active | Returns the active titlebar color |
| titlebar_active_text | Returns the active titlebar text color |
| titlebar_inactive | Returns the inactive titlebar color |
| titlebar_inactive_text | Returns the inactive titlebar text color |
| window_border_active | Returns the active window border color
| window_border_inactive | Returns the inactive window border color

You can also check if colored titlebars are enabled using `is_titlebar_colored` boolean.

---

### Get Start Menu or Taskbar color
You can get the Start Menu color from the `start_menu` variable and the Taskbar color from the `taskbar` variable. You can also check if they are colored or not using the `is_start_menu_colored` and `is_taskbar_colored` booleans.

---

### Get apps or system theme
This module also allows you to check if the apps or system use the light theme or not using the `apps_use_light_theme` and `system_uses_light_theme` booleans. The difference between them is that `apps_use_light_theme` is used to check the apps' theme and `system_uses_light_theme` is used to check the theme of some system components, such as the taskbar, Start menu and others. Here's an example:

```python
import winaccent

if winaccent.apps_use_light_theme: 
    print("Apps use light theme")
else: 
    print("Apps use dark theme")

if winaccent.system_uses_light_theme:
    print("System uses light theme")
else:
    print("System uses dark theme")
    
```

> [!NOTE]
> `apps_use_light_theme` and `system_uses_light_theme` will always return `True` on Windows 8.x.

---

### Check if transparency effects are enabled
You can check if the transparency effects are enabled using the `transparency_effects_enabled` boolean.

---

### Update values
The colors and settings values provided by this module can be updated manually using the ```update_values()``` function. This function will retrieve them again.

---

### Convert HEX color string to RGB tuple
This module has a function that allows you to convert a HEX color string to an RGB tuple. Useful if the GUI toolkit you're using expects using RGB tuples as colors instead of HEX string colors.

The function that does this is `hex_to_rgb()` and takes `hex` as an argument, where `hex` is the hex string color you want to convert to an RGB tuple. Here's how you can use it:

```python
import winaccent

# Prints (0, 120, 212) instead of #0078D4
print(winaccent.hex_to_rgb(winaccent.accent_normal))

# Prints (255, 255, 255) instead of #FFFFFF
print(winaccent.hex_to_rgb("#FFFFFF"))
```

---

### Appearance change listener
This module allows you to add a listener that will call a specific function when the accent color, active/inactive titlebar color, window border color or system theme changes. Here's how you can add it:

```python
import winaccent, threading

# Replace `callback` with the function that you want to be called
thread = threading.Thread(target = lambda: winaccent.on_appearance_changed(callback), daemon = True)
thread.start()
```

It also supports passing an `event` argument to your `callback` function if you need to only detect accent color, window chrome color or system theme changes. Your `callback` function needs to have an `event` argument and you must set the `pass_event` argument of the `on_appearance_changed()` function to `True`. Here's an example:

```python
import winaccent, threading

def detect_appearance_changes(event):
    if event == winaccent.event.accent_color_changed:
        print("Accent color changed!")
    elif event == winaccent.event.window_chrome_color_changed:
        print("One of the window chrome color changed!")
    elif event == winaccent.event.apps_theme_changed:
        print("Apps' theme changed!")
    elif event == winaccent.event.system_theme_changed:
        print("System theme changed!")

thread = threading.Thread(target = lambda: winaccent.on_appearance_changed(callback = detect_appearance_changes, pass_event = True), daemon = True)
thread.start()
```

Event constants (from the `event` class):

| Constant | Value |
|:---------|:-----:|
| accent_color_changed | 0 |
| window_chrome_color_changed | 1 |
| start_menu_color_changed | 2 |
| taskbar_color_changed | 3 |
| transparency_effects_toggled | 4 |
| apps_theme_changed | 5 |
| system_theme_changed | 6 |

> [!NOTE]
> If you added the listener, there's no need to call `update_values()` because it will be called automatically every time the appearance changes.

---

### Flags

Currently, there are only 2 flags available: `get_accent_from_dwm` and `dark_mode_titlebar` (both set to `False` by default). 

If `get_accent_from_dwm` flag is set to `True`, the `accent_normal` color will default to the active titlebar color (with maximum intensity on Windows 8.x) and different shades will be generated.

If `dark_mode_titlebar` flag is set to `True`, the dark mode titlebar-related colors will be returned. If it's set to `False`, it will return the light mode titlebar-related colors.

Here's an example of setting a flag to `True`:

```python
import winaccent

# Before enabling `dark_mode_titlebar` flag
print(winaccent.titlebar_active)

# Enable the flag and retrieve the values again
winaccent.dark_mode_titlebar = True
winaccent.update_values()

# After enabling `dark_mode_titlebar` flag
print(winaccent.titlebar_active)
```

> [!NOTE]
> You need to call `update_values()` after changing a flag's value for the changes to take effect.

<details>
<summary>Flag effects</summary>
<br>

Flag | If set to `False` (default) | If set to `True` |
|---|:---:|:---:|
get_accent_from_dwm | ![get_accent_from_dwm_off](https://github.com/Valer100/winaccent/blob/main/assets/dwm/get_accent_from_dwm_off.png?raw=true) | ![get_accent_from_dwm_on](https://github.com/Valer100/winaccent/blob/main/assets/dwm/get_accent_from_dwm_on.png?raw=true) |
dark_mode_titlebar | ![dark_mode_titlebar_off](https://github.com/Valer100/winaccent/blob/main/assets/dm_titlebar/dm_titlebar_off.png?raw=true) | ![dark_mode_titlebar_on](https://github.com/Valer100/winaccent/blob/main/assets/dm_titlebar/dm_titlebar_on.png?raw=true) |
</details>

## 💻 Demo
To see a demo, run the following command in your terminal (winaccent must be installed):

```python
python -m winaccent
```

This command has an optional `--mode` argument. It can take the following values:

| Value | Info |
|:------|:-----|
| gui | Shows a GUI demo. The GUI demo responds to accent color changes. |
| console | Shows a console demo. The console demo **does not** respond to accent color changes. |
| auto | If tkinter is installed and works correctly, a GUI demo will be shown. If that's not the case, a console demo will be shown. |

Example usage:

```
python -m winaccent --mode gui
```

The command will run with `--mode` set to `auto` by default.

<details>
<summary>Show GUI demo screenshots</summary>
<br>

| **Windows 11** | **Windows 10** | **Windows 8.x** |
|:--------------:|:--------------:|:---------------:|
| ![Windows 11 default](https://github.com/Valer100/winaccent/blob/main/assets/demo4/win11.png?raw=true) | ![Windows 10 default](https://github.com/Valer100/winaccent/blob/main/assets/demo4/win10.png?raw=true) | ![Windows 8 default](https://github.com/Valer100/winaccent/blob/main/assets/demo4/win8.png?raw=true) |

</details>

<details>
<summary>Show console demo output</summary>
<br>

```
Accent palette
==============

accent_light_3:                 #99EBFF
accent_light_2:                 #4CC2FF
accent_light_1:                 #0091F8
accent_normal:                  #0078D4
accent_dark_1:                  #0067C0
accent_dark_2:                  #003E92
accent_dark_3:                  #001A68


Window chrome
=============

is_titlebar_colored:            False
titlebar_active:                #F3F3F3
titlebar_active_text:           #000000
titlebar_inactive:              #F3F3F3
titlebar_inactive_text:         #929292
window_border_active:           #757575
window_border_inactive:         #757575


Start Menu
==========

is_start_menu_colored:          False
start_menu:                     #242424


Taskbar
=======

is_taskbar_colored:             False
taskbar:                        #1C1C1C


UI Appearance
=============

transparency_effects_enabled:   True
apps_use_light_theme:           False
system_uses_light_theme:        False


Other colors
============

accent_menu:                    #0078D4
```
</details>


## 🤩 Feedback
If you found a bug or want to make a suggestion, open a new issue. If you're ready to add a new feature or fix a bug, pull requests are welcome.

If you found this module useful, please consider starring this repository.
