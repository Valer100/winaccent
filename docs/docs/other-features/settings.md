# Settings

winaccent also allows you to retrieve some appearance-related settings. Here are all the settings that winaccent can retrieve right now:

## Colored title bars and window borders
This setting can be found on Windows 10 and 11 in Settings > Personalization > Color. It is called "Show accent color on title bars and window borders". To check if this setting is enabled or not, you can use the `is_titlebar_colored` boolean variable like this:

```python
import winaccent

if winaccent.is_titlebar_colored:
    print("The title bar and window borders are colored.")
else:
    print("The title bar and window borders aren't colored.")
```

!!! note
    On Windows 8.x, this variable will always return `True`.


## Colored taskbar and Start menu
This option can also be find on Windows 10 and 11 in Settings > Personalization > Color. It is called "Show accent color on Start and taskbar". To check if the Start menu or the taskbar is colored, you can use the `is_start_menu_colored` and `is_taskbar_colored` boolean variables like this:

```python
import winaccent

if winaccent.is_start_menu_colored:
    print("Start menu is colored.")
else:
    print("Start menu isn't colored.")

if winaccent.is_taskbar_colored:
    print("Taskbar is colored.")
else:
    print("Taskbar isn't colored.")
```

!!! question "Why is winaccent offering 2 different variables for this single setting in Windows?"
    At first, it might look confusing that winaccent offers `is_start_menu_colored` and `is_taskbar_colored` for the "Show accent color on Start and taskbar" setting that controls **both** the Start menu and the taskbar, but in the registry, the key that controls this setting is called `ColorPrevalence` and is located in `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize`. It can get the following values:

    | Value | Effect                                      |
    |:-----:|:--------------------------------------------|
    | 0     | Both Start menu and taskbar aren't colored. |
    | 1     | Both Start menu and taskbar are colored.    |
    | 2     | Only the taskbar is colored.                |

    The user can modify this value to their liking if they preffer none of them to be colorized, both of them, or only the taskbar. That's why winaccent offers 2 variables for checking if the Start menu or the taskbar is colored or not.

!!! note
    On Windows 8.x, these variables will always return `True`.


## Apps' and system's theme
The theme settings can be found on Windows 10 and 11 in Settings > Personalization > Color. The setting is called "Choose your mode" and the user can choose the theme of the system. It has a few options:

- Light
- Dark
- Custom (the user can change the theme of the system and the apps independently)

For detecting the apps' and the system's theme, winaccent offers 2 boolean variables: `apps_use_light_theme` and `system_uses_light_theme`. They can be used like this:

```python
import winaccent

if winaccent.apps_use_light_theme:
    print("The apps use the light theme")
else:
    print("The apps use the dark theme")

if winaccent.system_uses_light_theme:
    print("The system uses the light theme")
else:
    print("The system uses the dark theme")
```

!!! note
    On Windows 8.x, both `apps_use_light_theme` and `system_uses_light_theme` will always return `True`.


## Transparency effects
This setting can be found on Windows 10 and 11 in Settings > Personalization > Color or in Settings > Accessibility > Visual effects. The setting is called "Transparency effects" in both locations. To check if this setting is enabled or not, you can use the `transparency_effects_enabled` boolean variable like this:

```python
import winaccent

if winaccent.transparency_effects_enabled:
    print("Transparency effects are enabled.")
else:
    print("Transparency effects are disabled.")
```

!!! note
    On Windows 8.x, this variable will always return `True`