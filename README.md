<div align="center">
    <img width="700" src="https://github.com/Valer100/winaccent/blob/main/assets/hero.png?raw=true">
</div>

# winaccent
A simple and lightweight Python module for getting Windows' accent color. With this module you can also get shades of the accent color.

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
| accent_dark_mode | #4CC2FF | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark.png?raw=true"> |
| accent_normal | #0078D4 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_normal.png?raw=true"> |
| accent_light_mode | #0067C0 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light.png?raw=true"> |

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

print(winaccent.accent_light_mode) # Prints the light mode accent color
```

Here is a link for the guidelines (Microsoft Learn):

https://learn.microsoft.com/en-us/windows/apps/design/style/color#accent-color-palette

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

## 💻 Demo
To see a demo, run the following command in your terminal:

```python
python -m winaccent
```

Here's a demo with 3 different accent colors:

|**Blue** | **Green** | **Red**|
|:-------:|:---------:|:------:|
|![Blue](https://github.com/Valer100/winaccent/blob/main/assets/demo/demo_blue.png?raw=true) | ![Green](https://github.com/Valer100/winaccent/blob/main/assets/demo/demo_green.png?raw=true) | ![Red](https://github.com/Valer100/winaccent/blob/main/assets/demo/demo_red.png?raw=true) |


## 🤩 Feedback
If you found a bug or want to make a suggestion, open a new issue. If you're ready to add a new feature or fix a bug, pull requests are welcome.

If you find this module useful, you can consider starring this repository.

## 📋 To do
- [x] ~~Add an accent color change listener~~
