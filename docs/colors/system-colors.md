# System colors

## Taskbar and Start Menu color

winaccent can also retrieve the taskbar and Start menu colors. You can do that using the `start_menu` and `taskbar` variables. Here is an example:

```python
import winaccent

print(f"Taskbar color: {winaccent.taskbar}")
print(f"Start menu color: {winaccent.start_menu}")
```

These variables can also return the right colors if the "Show accent color on Start and taskbar" is enabled in Settings > Personalization > Colors.

!!! note
    You can also check if the Start menu and taskbar are colored using the `is_start_menu_colored` and `is_taskbar_colored` booleans. See [Colored taskbar and Start menu](../other-features/settings.md#colored-taskbar-and-start-menu) for more information.

!!! warning
    On Windows 8.x, the taskbar color will be returned without opacity to prevent some issues.


## Menu accent color

The accent color used in lockscreen, UAC (Windows 10), welcome screen, start menu (Windows 8.x), Metro dialogs and other elements is called the **menu accent color** (`AccentMenu` in the registry). You can get this accent color using the `accent_menu` variable (usually it's the same color as `accent_normal`, but can be modified in the registry). Here's an example:

```python
import winaccent

print(f"Menu accent color: {winaccent.accent_menu}")
```