from setuptools import setup, find_packages

description = open("README.md", "r", encoding = "utf8").read()

setup(
    name = "winaccent",
    version = "1.1.0",
    license = "MIT",
    author = "Valer100",
    maintainer = "Valer100",
    description = "A simple and lightweight Python module for getting Windows' accent color or a shade of it. Works on both Windows 10 and 11 and doesn't require additional dependencies.",
    url = "https://github.com/Valer100/winaccent",
    project_urls = {
        "Source": "https://github.com/Valer100/winaccent",
        "Issues": "https://github.com/Valer100/winaccent/issues",
    },
    packages = find_packages(),
    long_description = description,
    long_description_content_type = "text/markdown",
    classifiers = [
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 11",
    ],
    keywords = [
        "accent",
        "accent_light",
        "accent_dark",
        "accent_color"
        "theme",
        "tk",
        "ttk",
        "tkinter",
        "modern",
        "fluent",
        "sun-valley",
        "windows-11",
        "windows-10",
        "winui",
        "winaccent"
    ],
)
