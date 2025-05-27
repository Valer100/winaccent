# Example usage

## Printing the accent color
winaccent is very easy to use. Here's how we can print the accent color the system is using:

```python
import winaccent

print(f"Accent color: {winaccent.accent_normal}")
```

Simple as that.


## Using winaccent in cross-platform applications
Unfortunately, winaccent is a Windows-only module, meaning that it won't work on other platforms like Linux or MacOS. Trying to import winaccent on a platform other than Windows or a Windows version older than 8.0 will raise an `ImportError` exception. When using this module in cross-platform applications, make sure you only import and use winaccent on Windows systems to avoid errors. For other operating systems, you will need to find other ways to get the system's accent color or hardcode it to a different color. Here's an example:

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

If you're using a Python version that supports Windows versions older than 8.0 (Python 3.8 and older), use the following example:

```python
import sys

if sys.platform == "win32":
    # Get Windows version (major.minor)
    windows_version = sys.getwindowsversion()
    current_version = float(f"{windows_version.major}.{windows_version.minor}")

    # Check if the Windows version is greater than or equal to 6.2 (Windows 8.0)
    # Windows 8.1 will return 6.3 and Windows 10 and 11 will return 10.0
    if current_version >= 6.2:
        import winaccent
        print(winaccent.accent_normal)
else:
    # Other platforms
    #
    # You will need to find different ways for retrieving the
    # system accent color or hardcode it to a different color.

    print("The script is running on an unsupported platform.")
```