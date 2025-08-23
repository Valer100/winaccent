<div id="toc">
    <ul style="list-style: none; padding: 0px;">
        <h1>
            <summary>
                <h><img src="https://raw.githubusercontent.com/Valer100/winaccent/refs/heads/main/assets/logo/logo_fluent.svg" height=100 alt="winaccent logo" align="left"/><h3>winaccent</h3></h>
            </summary>
            <p></p>
        </h1>
    </ul>
</div>
<br>

[![PyPI](https://img.shields.io/pypi/v/winaccent)](https://pypi.org/project/winaccent/)
[![Python](https://img.shields.io/badge/python-3.6+-blue)]()
[![Windows](https://img.shields.io/badge/windows-vista+-blue)]()
[![Format](https://img.shields.io/pypi/format/winaccent)](https://pypi.org/project/winaccent/)
[![Downloads](https://img.shields.io/pepy/dt/winaccent)](https://pypi.org/project/winaccent/)
[![Stars](https://img.shields.io/github/stars/Valer100/winaccent?style=flat&color=yellow)](https://github.com/Valer100/winaccent/stargazers)
[![Contributors](https://img.shields.io/github/contributors/Valer100/winaccent)](https://github.com/Valer100/winaccent/graphs/contributors)
[![Last commit](https://img.shields.io/github/last-commit/Valer100/winaccent)](https://github.com/Valer100/winaccent/commits/main)
[![Commits since latest release](https://img.shields.io/github/commits-since/Valer100/winaccent/latest)](https://github.com/Valer100/winaccent/commits/main)
[![License](https://img.shields.io/github/license/Valer100/winaccent)](https://github.com/Valer100/winaccent/blob/main/LICENSE)
[![Documentation](https://img.shields.io/badge/documentation-here-blue)](https://valer100.github.io/winaccent)

A simple and lightweight Python module for easily retrieving Windows' accent color, including shades, specific window chrome colors such as active/inactive titlebar and window borders and theme. Supports Windows 8.x, 10 and 11 and doesn't require additional dependencies.

## 📝 Requirements
- Windows Vista or later (Windows 8.0 or later required for full functionality)
- Python 3.6 or later

## 📦 Installation
Run this command in your terminal:

```
pip install winaccent
```

To update the module, run this command:

```
pip install --upgrade winaccent
```

## 📜 Documentation
The documentation is available [here](https://valer100.github.io/winaccent).

## 💻 Demo
To see a demo, run the following command in your terminal (winaccent must be installed):

```powershell
python -m winaccent
```

... or even simpler:

```powershell
winaccent
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


| Windows version | Light mode | Dark mode |
|:---------------:|:----------:|:---------:|
| Windows 11      | ![Windows 11 default](https://github.com/Valer100/winaccent/blob/main/assets/demo4/win11.png?raw=true) | ![Windows 11 default dark](https://github.com/Valer100/winaccent/blob/main/assets/demo4/win11_dark.png?raw=true) |
| Windows 10      | ![Windows 10 default](https://github.com/Valer100/winaccent/blob/main/assets/demo4/win10.png?raw=true) | ![Windows 10 default dark](https://github.com/Valer100/winaccent/blob/main/assets/demo4/win10_dark.png?raw=true) |
| Windows 8.x     | ![Windows 8.x default](https://github.com/Valer100/winaccent/blob/main/assets/demo4/win8.png?raw=true) | |
| Windows 7       | ![Windows 7 default](https://github.com/Valer100/winaccent/blob/main/assets/demo4/win7.png?raw=true) | |
| Windows Vista   | ![Windows vista default](https://github.com/Valer100/winaccent/blob/main/assets/demo4/winvista.png?raw=true) | |


</details>

<details>
<summary>Show console demo output</summary>
<br>

```
winaccent 2.2.0
===============

This Windows version is fully supported.


Accent palette
--------------

accent_light_3:               #99EBFF
accent_light_2:               #4CC2FF
accent_light_1:               #0091F8
accent_normal:                #0078D4
accent_dark_1:                #0067C0
accent_dark_2:                #003E92
accent_dark_3:                #001A68

accent_menu:                  #0078D4


Window chrome
-------------

is_titlebar_colored:          False
titlebar_active:              #F3F3F3
titlebar_active_text:         #000000
titlebar_inactive:            #F3F3F3
titlebar_inactive_text:       #929292
window_border_active:         #757575
window_border_inactive:       #757575


Start Menu
----------

is_start_menu_colored:        False
start_menu:                   #242424


Taskbar
-------

is_taskbar_colored:           False
taskbar:                      #1C1C1C
is_taskbar_center_aligned:    True
is_taskbar_auto_hiding:       False


UI Appearance
-------------

transparency_effects_enabled: True
apps_use_light_theme:         False
system_uses_light_theme:      False


Environment
-----------

Windows 11 Professional (Build 26100.4946)
Python 3.11.9 (final)
Loaded submodule: _win_10.py
Full support: True
```
</details>


## 🤩 Feedback
If you found a bug or want to make a suggestion, open a new issue. If you're ready to add a new feature or fix a bug, pull requests are welcome.

If you found this module useful, please consider starring this repository.
