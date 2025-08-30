# Changelog

<!-- ## <font class="version-testing"><font title="Work in progress">:material-flask-outline:</font> Version 2.1.0</font> <small>(not released yet)</small> { id="2.1.0" } -->

## <font class="version-latest"><font title="Latest version">:material-check:</font> Version 2.2.0</font> <small>(not released yet)</small> { id="2.2.0" }

## <font title="Released">:material-tag-outline:</font> Version 2.1.0 <small>(June 24, 2025)</small> { id="2.1.0" }

### New features
- Added 2 flags: `GET_ACCENT_FROM_DWM` and `DARK_MODE_WINDOW`
- Now you can retrieve the active/inactive titlebar text color from the `titlebar_active_text` and `titlebar_inactive_text` variables.
- Now you can retrieve the actual active/inactive titlebar color regardless if the "Show accent color on title bars and window borders" setting is enabled or not.
- Now you can retrieve the inactive window border color using `window_border_inactive`. For retrieving the active window border color, use `window_border_active`. `window_border` will be deprecated starting with version 3.0.0.
- Now you can retrieve the start menu and taskbar color using `start_menu` and `taskbar` (you can also check if they are colored or not using `is_start_menu_colored` and `is_taskbar_colored` booleans).

### Improvements
- Redesigned the GUI demo to look better and cleaner.
- New documentation website (this one).

### Regressions
- Compatibility with Python 3.6 and 3.7 is broken (will be fixed in the next update).


## <font title="Released">:material-tag-outline:</font> Version 2.0.1 <small>(October 21, 2024)</small> { id="2.0.1" }

### Breaking changes
- The minimum Python version supported was changed to 3.6
- The module will now raise an `ImportError` exception instead of an `UnsupportedPlatfromException` exception
- `on_accent_changed_listener` function was renamed to `on_appearance_changed`
- `update_accent_colors` function was renamed to `update_values`

### New features
- Added Windows 8.x support
- Added a function to convert HEX colors to RGB tuples (`hex_to_rgb`)
- Retrieve apps' theme and system's theme using `apps_use_light_theme` and `system_uses_light_theme` booleans

### Fixes
- Get the right `window_border` color in Windows 10 and 11
- Use placeholder values if the registry keys for some values do not exist
- More optimizations and improvements

### What happened to v2.0.0?
Well, that version had a bug that I didn't notice. The `system_uses_light_theme` boolean was returning the wrong value for the current system theme. This is fixed in v2.0.1.


## <font title="Released">:material-tag-outline:</font> Version 1.1.0 <small>(September 26, 2024)</small> { id="1.1.0" }

### What's new
- Now you can check if the "Show accent color on title bars and window borders" option from Settings > Personalization > Color is enabled using the `is_titlebar_colored` boolean.
- New colors added: `titlebar_active`, `titlebar_inactive`, `window_border` and `accent_menu`.
- Some demo improvements.


## <font title="Released">:material-tag-outline:</font> Version 1.0.1 <small>(September 9, 2024)</small> {id="1.0.1"}

### What's new
- Raise a `winaccent.UnsupportedPlatformException` exception when the module is imported on a different OS than Windows and Windows versions older than 10.
- `winreg` module won't be imported anymore on platforms other than Windows
- Now `python -m winaccent` supports an optional `--mode` argument.


## <font title="Released">:material-tag-outline:</font> Version 1.0.0 <small>(September 1, 2024)</small> { id="1.0.0" }

### Breaking changes
`accent_light` was renamed to `accent_dark` and `accent_dark` to `accent_light` to reflect the lightness/darkness of the color. This means that after upgrading to 1.0.0 these colors will be inverted.

The easiest fix for this is to replace all occurences of `accent_light` with `accent_light_mode` and `accent_dark` with `accent_dark_mode`. 

`accent_light_mode` and `accent_dark_mode` variables are named to reflect the theme (light/dark mode) and work the same way like `accent_light` and `accent_dark` variables from previous versions.

### What's new
- Added accent color shades.
- When running `python -m winaccent` in terminal a window with the current accent palette will be shown


## <font title="Released">:material-tag-outline:</font> Version 0.3.0 <small>(August 19, 2024)</small> { id="0.3.0" }

### What's new
- Added accent color change listener


## <font title="Released">:material-tag-outline:</font> Version 0.2.0 <small>(August 18, 2024)</small> { id="0.2.0" }

### What's new:
- Removed dependency on `darkdetect` (this means that `accent_auto` is now deprecated)
- Added a new function: `update_accent_colors`


## <font title="Released">:material-tag-outline:</font> Version 0.1.0 <small>(August 16, 2024)</small> { id="0.1.0" }

The first version ever released.