# Windows Vista and 7 compatibility

winaccent supports Windows Vista and 7, but not completely. Some features aren't supported and won't be available when winaccent is running on these Windows versions. Most of the time, unsupported variables will return `None` on these versions.

The accent palette is generated from the current window color using the same custom algorithm that's used on Windows 8.x for generating the palette.


## Using winaccent on Windows Vista and 7
Python versions older than 3.8 support Windows Vista and 7. For checking if the Windows version is fully supported by winaccent, you can use the `os_has_full_support` boolean variable. Here's an example:

```python
import winaccent

if winaccent.os_has_full_support:
    # The Windows version has full support (Windows 8.0 +)
    # 'winaccent.start_menu' is supported and will return here the start menu color

    print(winaccent.start_menu)
else:
    # The Windows version has limited support (Windows Vista or Windows 7)
    # 'winaccent.start_menu' isn't supported and will return `None`

    print("'winaccent.start_menu' isn't supported on this Windows version.")
```

## Supported and unsupported features
Here is the list of the supported and unsupported features on these Windows versions:

### Supported features
- [Accent color and shades](../colors/accent-color-and-shades.md) (all)
- [Settings](../other-features/settings.md) (all)
- [Appearance change listener and manual values refreshing](../other-features/refreshing-the-colors-and-listener.md)
- [HEX string color to RGB integer tuple function](../other-features/hex-to-rgb-function.md)

### Unsupported features
- [System colors](../colors/system-colors.md) (except `accent_menu`)
- [Window chrome colors](../colors/window-chrome-colors.md)
- [Flags](../other-features/flags.md) (all)