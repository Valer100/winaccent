# Refreshing the colors and the appearance change listener
By default, when you import the module, winaccent retrieves the colors and settings only once. This means the variables will not update if the colors or settings change after the module is imported. While it would be possible to use functions instead of variables, the current approach helps prevent inconsistencies in colors and settings before and after they change while your app is running.

Consider this example: Your user runs your app with the apps' theme set to dark and the system's accent color set to blue. While the app is running, they change the apps' theme to light and the system's accent color to green. If winaccent used functions, opening a new window in your app would cause the new window to follow the updated settings, but the main window would still use the old settings, unless you set up the appearance change listener. With variables, both the main and new windows will continue to use the old settings unless the listener is set up.

## Refreshing the colors manually
In some cases, refreshing the colors and settings would be the best. To update all the colors and settings, you can call the `update_values()` function. Here's an example of how you can use it:

```python
import winaccent

print(f"Current accent color: {winaccent.accent_normal}")
input("Change the system's accent color, then press Enter to see the new color...")

winaccent.update_values()
print(f"New accent color: {winaccent.accent_normal}")
```

## Appearance change listener
In GUI apps, for making the app responsive to the system's appearance settings, winaccent also includes an **appearance change listener**. It can be used like this:

```python
import winaccent, threading

def when_appearance_changed():
    print(f"Accent color changed to {winaccent.accent_normal}")
    print(f"Apps' theme changed to {'light' if winaccent.apps_use_light_theme else 'dark'}")

thread = threading.Thread(target = lambda: winaccent.on_appearance_changed(callback = when_appearance_changed), daemon = True)
thread.start()
```

The example code above prints the accent color and the apps' theme when the appearance settings change. But they will only be printed when any appearance setting supported by winaccent changes. This means that the code above will print the accent color and the apps' theme even if they don't actually change, but other settings like the colored title bars and window borders do. To fix this, we will have to add a new `event` integer argument to the `when_appearance_changed()` function, check if `event` is equal to an event constant (more constants bellow) and set the `pass_event` argument of the `on_appearance_changed()` function to `True`. Here's an example:

```python
import winaccent, threading

def when_appearance_changed(event):
    if event == winaccent.Event.ACCENT_COLOR_CHANGED:
        print(f"Accent color changed to {winaccent.accent_normal}")
    elif event == winaccent.Event.APPS_THEME_CHANGED:
        print(f"Apps' theme changed to {'light' if winaccent.apps_use_light_theme else 'dark'}")

thread = threading.Thread(target = lambda: winaccent.on_appearance_changed(callback = when_appearance_changed, pass_event = True), daemon = True)
thread.start()
```

In this example, the accent color will only be printed if it changes. The same goes for the apps' theme.

Here are all the supported event constants from the `Event` class:

| Constant                     | Value |
|:-----------------------------|:-----:|
| ACCENT_COLOR_CHANGED         | 0     |
| WINDOW_CHROME_COLOR_CHANGED  | 1     |
| START_MENU_COLOR_CHANGED     | 2     |
| TASKBAR_COLOR_CHANGED        | 3     |
| TRANSPARENCY_EFFECTS_TOGGLED | 4     |
| APPS_THEME_CHANGED           | 5     |
| SYSTEM_THEME_CHANGED         | 6     |

!!! note
    If you set up the listener, there's no need to call `update_values()` manually, because the values will update automatically.

Here is a demonstration of the appearance change listener:

<video controls>
    <source src="../assets/appearance-listener-demo.mp4" type="video/mp4">
</video>