# Version 2.2.0

## What's new

- Added limited support for Windows Vista and 7
- Added a much simpler command for running the demo program: `winaccent` (it also supports the same arguments as the `python -m winaccent` command)

## Fixes and improvements

- Fixed compatibility with Python 3.6 and 3.7
- Fixed demo program not launching at all (even in console mode) if the Python installation was missing tk/tcl support
- Add dark mode support to the demo program (Windows 10+)
- Add color preview and use different text colors for category titles and booleans in the console demo (Windows 10+)