<div align="center">
    <img width="700" src="https://github.com/Valer100/winaccent/blob/main/assets/hero.png?raw=true">
</div>

# winaccent
[![PyPI](https://img.shields.io/pypi/v/winaccent)](https://pypi.org/project/winaccent/)
[![Python](https://img.shields.io/badge/python-3.6+-blue)]()
[![Windows](https://img.shields.io/badge/windows-8.0+-blue)]()
[![Downloads](https://img.shields.io/pepy/dt/winaccent)](https://pypi.org/project/winaccent/)
[![Stars](https://img.shields.io/github/stars/Valer100/winaccent?style=flat&color=yellow)]()
[![Contributors](https://img.shields.io/github/contributors/Valer100/winaccent)]()
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

| Variable | Color | Preview |
|----------|:-------:|:-------:|
| accent_dark_mode<br>(or accent_light) | #4CC2FF | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark.png?raw=true"> |
| accent_normal | #0078D4 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_normal.png?raw=true"> |
| accent_light_mode<br>(or accent_dark) | #0067C0 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light.png?raw=true"> |

If you need a different shade, you can get it from one of these variables:

| Variable | Color | Preview |
|----------|:-------:|:-------:|
| accent_light_3 | #99EBFF | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark_3.png?raw=true"> |
| accent_light_2 | #4CC2FF | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark.png?raw=true"> |
| accent_light_1 | #0091F8 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark_1.png?raw=true"> |
| accent_normal | #0078D4 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_normal.png?raw=true"> |
| accent_dark_1 | #0067C0 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light.png?raw=true"> |
| accent_dark_2 | #003E92 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light_2.png?raw=true"> |
| accent_dark_3 | #001A68 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light_3.png?raw=true"> |

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

### Get active/inactive titlebar color or window border color

> [!WARNING]
> The colors provided by these variables are the colors used by Windows to colorize the titlebar and the window borders when the "Show accent color on title bars and window borders" option is enabled in Settings.
> <br><br>
> <img src="https://github.com/Valer100/winaccent/blob/main/assets/show_accent_color_on_window_stuff.png?raw=true">
> <br><br>
> Also, the `titlebar_active` and `window_border` variables don't always return the same color. The user can change the color of the titlebar or window borders from the registry. <br><br>
> <img src="https://github.com/Valer100/winaccent/blob/main/assets/custom_window_colors_demo.png?raw=true">

You can get the active titlebar color from `titlebar_active` variable and the inactive titlebar color from `titlebar_inactive`. The window border color can be obtained from `window_border` variable.

You can also check if colored titlebars are enabled using `is_titlebar_colored` boolean.

> [!NOTE]
> `titlebar_inactive` will return `None` if the inactive titlebar color isn't set (this is usually done via registry).

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

> [!NOTE]
> If you added the listener, there's no need to call `update_values()` because it will be called automatically every time the appearance changes.

Here's a demo:

https://github.com/user-attachments/assets/c77e3219-fa44-4026-bbc3-1995358f4c7e

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

Here's how a GUI demo looks:

| **Windows version** | **Default colors & settings** | **Modified colors & settings** |
|:-------------------:|:------------------:|:----------------------------:|
| **Windows 11** | ![Windows 11 default](https://github.com/Valer100/winaccent/blob/main/assets/demo2/win_11_default.png?raw=true) | ![Windows 11 modified](https://github.com/Valer100/winaccent/blob/main/assets/demo2/win_11_modified.png?raw=true)
| **Windows 10** | ![Windows 10 default](https://github.com/Valer100/winaccent/blob/main/assets/demo2/win_10_default.png?raw=true) | ![Windows 10 modified](https://github.com/Valer100/winaccent/blob/main/assets/demo2/win_10_modified.png?raw=true)
| **Windows 8** | ![Windows 8 default](https://github.com/Valer100/winaccent/blob/main/assets/demo2/win_8_default.png?raw=true) | ![Windows 8 modified](https://github.com/Valer100/winaccent/blob/main/assets/demo2/win_8_modified.png?raw=true)

A console demo looks like this (for default blue accent color):

```
Accent palette
==============

accent_light_3:           #99EBFF
accent_light_2:           #4CC2FF
accent_light_1:           #0091F8
accent_normal:            #0078D4
accent_dark_1:            #0067C0
accent_dark_2:            #003E92
accent_dark_3:            #001A68


Windows options
===============

is_titlebar_colored:      False
titlebar_active:          #0078D4
titlebar_inactive:        None
window_border:            #0078D4


System theme
============

apps_use_light_theme:     False
system_uses_light_theme:  False


Other colors
============

accent_menu:              #0078D4
```


## 🤩 Feedback
If you found a bug or want to make a suggestion, open a new issue. If you're ready to add a new feature or fix a bug, pull requests are welcome.

If you found this module useful, please consider starring this repository.

## 📋 To do
- [x] ~~Add an accent color change listener~~
- [x] ~~Add color shades~~
- [x] ~~Add support for getting active/inactive titlebar color~~
- [x] ~~Add support for getting window border color~~
- [x] ~~Add support for Windows 8.x~~
- [x] ~~Add support for retrieving apps' and system's theme~~