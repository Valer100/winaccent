<div align="center">
    <img width="700" src="https://github.com/Valer100/winaccent/blob/main/assets/hero.png?raw=true">
</div>

# winaccent
A simple and lightweight Python module for getting Windows' accent color. With this module you can get both light and dark mode accent colors.

## 📦 Installation
Run this command in your terminal:

```
pip install winaccent
```

## 📜 Documentation

### Get a specific accent color

| Variable | Info |
|----------|------|
| accent_light | Returns the light mode accent color
| accent_dark | Returns the dark mode accent color
| accent_normal | Returns the normal accent color

Example:

```python
import winaccent

print(winaccent.accent_light) # Prints the light mode accent color
```

### Update accent colors

The accent colors can be updated manually using the ```update_accent_colors()``` function. This function will retrieve the values again.

### Accent color change listener
This module allows you to add a listener that will call a specific function when the accent color changes. Here's how you can add it:

```python
import winaccent, threading

# Replace `callback` with the function that you want to be called
thread = threading.Thread(target = lambda: winaccent.on_accent_changed_listener(callback), daemon = True)
thread.start()
```

> [!NOTE]
> If you added the listener, there's no need to call `update_accent_colors` because it will be called automatically every time the accent color changes.

## 🖥️ Output
Here is the output for the default (blue) accent color on Windows 11:

| Variable | Color | Preview |
|----------|:-------:|:-------:|
| accent_light | #0067C0 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light.png?raw=true"> |
| accent_dark | #4CC2FF | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark.png?raw=true"> |
| accent_normal | #0078D4 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_normal.png?raw=true"> |

Here is the output for a custom accent color (green):


| Variable | Color | Preview |
|----------|:-------:|:-------:|
| accent_light | #007300 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light_green.png?raw=true"> |
| accent_dark | #3FFF24 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark_green.png?raw=true"> |
| accent_normal | #008B00 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_normal_green.png?raw=true"> |

## 📋 To do
- [x] ~~Add an accent color change listener~~