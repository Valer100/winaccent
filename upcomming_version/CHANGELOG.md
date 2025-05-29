# Version 2.1.0

## New features
- Added 2 flags: `get_accent_from_dwm` and `dark_mode_window`
- Now you can retrieve the active/inactive titlebar text color from the `titlebar_active_text` and `titlebar_inactive_text` variables.
- Now you can retrieve the actual active/inactive titlebar color regardless if the "Show accent color on title bars and window borders" setting is enabled or not.
- Now you can retrieve the inactive window border color using `window_border_inactive`. For retrieving the active window border color, use `window_border_active`. `window_border` will be deprecated starting with version 3.0.0.
- Now you can retrieve the start menu and taskbar color using `start_menu` and `taskbar` (you can also check if they are colored or not using `is_start_menu_colored` and `is_taskbar_colored` booleans).

[Read the documentation](https://valer100.github.io/winaccent) to learn more about the new features.

## Improvements
- Redesigned the GUI demo to look better and cleaner.
- New documentation website (you can visit it [here](https://valer100.github.io/winaccent)).

<br>

> [!NOTE]
> To update, run the following command:
>
> ```
> pip install --upgrade --nocache winaccent
> ```