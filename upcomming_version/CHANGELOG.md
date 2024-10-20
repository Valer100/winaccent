# Version 2.0.0

## Breaking changes
- The minimum Python version supported was changed to 3.6
- The module will now raise an `ImportError` exception instead of an `UnsupportedPlatfromException` exception
- `on_accent_changed_listener()` function was renamed to `on_appearance_changed()`
- `update_accent_colors()` function was renamed to `update_values()`

## New features
- Added Windows 8.x support
- Added a function to convert HEX colors to RGB tuples (`hex_to_rgb()`)
- Retrieve apps' theme and system's theme using `apps_use_light_theme` and `system_uses_light_theme` booleans

Read the documentation to learn more about the new features.

## Fixes
- Get the right `window_border` color in Windows 10 and 11
- Use placeholder values if the registry keys for some values do not exist
- More optimizations and improvements

<br>

> [!NOTE]
> To update, run the following command:
>
> ```
> pip install --upgrade winaccent
> ```