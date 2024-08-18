<div align="center">
    <img width="700" src="https://github.com/Valer100/winaccent/blob/main/assets/hero.png?raw=true">
</div>

# winaccent
A simple Python module for getting Windows' accent color. With this module you can get both light and dark mode accent colors.

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

The accent colors can be updated using the ```update_accent_colors()``` function.

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
- [ ] Add an accent color change listener