# Example usage

## Printing the accent color
winaccent is very easy to use. Here's how we can print the accent color the system is using:

```python
import winaccent

print(f"Accent color: {winaccent.accent_normal}")
```

Simple as that.


## Using winaccent in cross-platform applications
Unfortunately, winaccent is a Windows-only module, meaning that it won't work on other platforms like Linux or MacOS. Trying to import winaccent on a platform other than Windows or a Windows version older than Windows Vista will raise an `ImportError` exception. When using this module in cross-platform applications, make sure you only import and use winaccent on Windows systems to avoid errors. For other operating systems, you will need to find other ways to get the system's accent color or hardcode it to a different color. Here's an example:

```python
import sys

if sys.platform == "win32":
    # Windows

    import winaccent
    print(winaccent.accent_normal)
else:
    # Other platforms
    #
    # You will need to find different ways for retrieving the
    # system accent color or hardcode it to a different color.

    print("The script is running on an unsupported platform.")
```

## Using winaccent on Windows Vista and 7
Python versions older than 3.8 support Windows Vista and 7. If you're using a Python version older than 3.8 and you want to support these Windows versions, you need to know that they aren't fully supported by winaccent and only some features will be available. For checking if the Windows version is fully supported by winaccent, you can use the `os_has_full_support` boolean variable. Here's an example:

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

For the full list of supported and unsupported features, see [Windows Vista and 7 compatibility](../other-features/windows_vista_and_7_compatibility.md).