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

> [!NOTE]
> The color previews shown here are for the Windows 11's default accent color (blue).

For simplicity, you can get a specific accent color from one of the following variables:

| Variable | Color | Preview |
|----------|:-------:|:-------:|
| accent_light | #4CC2FF | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark.png?raw=true"> |
| accent_normal | #0078D4 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_normal.png?raw=true"> |
| accent_dark | #0067C0 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light.png?raw=true"> |

If you need a different shade of the accent color, you can get it from one of these variables:

| Variable | Color | Preview |
|----------|:-------:|:-------:|
| accent_light_3 | #99EBFF | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark_3.png?raw=true"> |
| accent_light_2 | #4CC2FF | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark.png?raw=true"> |
| accent_light_1 | #0091F8 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark_1.png?raw=true"> |
| accent_normal | #0078D4 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_normal.png?raw=true"> |
| accent_dark_1 | #0067C0 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light.png?raw=true"> |
| accent_dark_2 | #003E92 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light_2.png?raw=true"> |
| accent_dark_3 | #001A68 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light_3.png?raw=true"> |



Example:

```python
import winaccent

print(winaccent.accent_light) # Prints the light accent color
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
> If you added the listener, there's no need to call `update_accent_colors()` because it will be called automatically every time the accent color changes.

Here's a demo:

![Listener demo](https://github.com/Valer100/winaccent/blob/main/assets/listener_demo.gif?raw=true)

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

## 🤩 Feedback
If you found a bug or want to make a suggestion, open a new issue. If you're ready to add a new feature or fix a bug, pull requests are welcome.

If you find this module useful, you can consider starring this repository.

## 📋 To do
- [x] ~~Add an accent color change listener~~
