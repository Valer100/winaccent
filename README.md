<div align="center">
    <img width="700" src="https://github.com/Valer100/winaccent/blob/main/assets/hero.png?raw=true">
</div>

# winaccent
A simple and lightweight Python module for getting Windows' accent color or a shade of it. Works on both Windows 10 and 11 and doesn't require additional dependencies.

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

### Get a specific accent color

> [!NOTE]
> The color values and previews shown here are for Windows 11's default accent color (blue). If you have a different accent color, you'll get the color values based on your accent color.

For simplicity, you can get a specific accent color from one of the following variables:

| Variable | Color | Preview |
|----------|:-------:|:-------:|
| accent_dark_mode | #4CC2FF | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark.png?raw=true"> |
| accent_normal | #0078D4 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_normal.png?raw=true"> |
| accent_light_mode | #0067C0 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light.png?raw=true"> |

If you need a different shade, you can get it from one of these variables:

| Variable | Color | Preview |
|----------|:-------:|:-------:|
| accent_light_3 | #99EBFF | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark_3.png?raw=true"> |
| accent_light_2 | #4CC2FF | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark.png?raw=true"> |
| accent_light_1 | #0091F8 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_dark_1.png?raw=true"> |
| accent_normal | #0078D4 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_normal.png?raw=true"> |
| accent_dark_1 | #0067C0 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light.png?raw=true"> |
| accent_dark_2 | #003E92 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light_2.png?raw=true"> |
| accent_dark_3 | #001A68 | <img src="https://github.com/Valer100/winaccent/blob/main/assets/colors/accent_light_3.png?raw=true"> |


> [!TIP]
> `accent_dark_mode` is the same thing as `accent_light` which is the same thing as `accent_light_2`. 
>
> Also, `accent_light_mode` is the same thing as `accent_dark` which is the same thing as `accent_dark_1`.

Example:

```python
import winaccent

print(winaccent.accent_light_mode) # Prints the light mode accent color
```

You may want to take a look at Microsoft's accent color guidelines. You can do that [here](https://learn.microsoft.com/en-us/windows/apps/design/style/color#accent-color-palette).

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

![Listener demo](https://github.com/Valer100/winaccent/blob/main/assets/listener_demo.mp4?raw=true)

## 💻 Demo
To see a demo, run the following command in your terminal (winaccent must be installed):

```python
python -m winaccent
```

Here's a demo with 6 different accent colors:

| **Blue** | **Dark green** | **Red** |
|:-------:|:---------:|:------:|
|![Blue](https://github.com/Valer100/winaccent/blob/main/assets/demo/demo_blue.png?raw=true) | ![Dark green](https://github.com/Valer100/winaccent/blob/main/assets/demo/demo_green.png?raw=true) | ![Red](https://github.com/Valer100/winaccent/blob/main/assets/demo/demo_red.png?raw=true) |
| **Gold** | **Iris pastel** | **Camouflage desert** |
|![Gold](https://github.com/Valer100/winaccent/blob/main/assets/demo/demo_orange.png?raw=true) | ![Iris pastel](https://github.com/Valer100/winaccent/blob/main/assets/demo/demo_purple.png?raw=true) | ![Camouflage desert](https://github.com/Valer100/winaccent/blob/main/assets/demo/demo_tan.png?raw=true) |


## 🤩 Feedback
If you found a bug or want to make a suggestion, open a new issue. If you're ready to add a new feature or fix a bug, pull requests are welcome.

If you find this module useful, you can consider starring this repository.

## 📋 To do
- [x] ~~Add an accent color change listener~~
- [x] ~~Add color shades~~
- [ ] Do some research about a weird color (see line 42 in `winaccent/__init__.py`)
