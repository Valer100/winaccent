# HEX string color to RGB integer tuple function

By design, winaccent color variables return colors in the RGB HEX strings format (`#RRGGBB`). However, this format might not be suitable for other modules or things, so winaccent also includes a `hex_to_rgb()` function that takes `hex` as a string argument (the RGB HEX string color) and returns the RGB integer tuple of that color. It can be used like this:

```python
import winaccent

# Prints (0, 120, 212) instead of #0078D4
print(winaccent.hex_to_rgb(winaccent.accent_normal))
```

It also works with colors that are not provided by winaccent:

```python
import winaccent

# Prints (255, 255, 255) instead of #FFFFFF
print(winaccent.hex_to_rgb("#FFFFFF"))
```