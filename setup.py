from setuptools import setup, find_packages

description = open("README.md", "r", encoding = "utf8").read()

setup(
    name = "winaccent",
    version = "2.2.0",
    license = "MIT",
    author = "Valer100",
    maintainer = "Valer100",
    description = "A simple and lightweight Python module for easily retrieving Windows' accent color, including shades, specific window chrome colors such as active/inactive titlebar and window borders and theme. Supports Windows Vista, 7, 8.x, 10 and 11 and doesn't require additional dependencies.",
    url = "https://github.com/Valer100/winaccent",
    python_requires = ">=3.6",
    project_urls = {
        "Source": "https://github.com/Valer100/winaccent",
        "Documentation": "https://valer100.github.io/winaccent",
        "Changelog": "https://valer100.github.io/winaccent/about/changelog",
        "Issues": "https://github.com/Valer100/winaccent/issues",
    },
    packages = find_packages(),
    entry_points = {
        "console_scripts": [
            "winaccent = winaccent.__main__:main",
        ],
    },
    package_data = {
        "winaccent": ["icon.ico"]
    },
    long_description = description,
    long_description_content_type = "text/markdown",
    classifiers = [
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows Vista",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows 8",
        "Operating System :: Microsoft :: Windows :: Windows 8.1",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 11",
    ],
    keywords = [
        "accent",
        "accent-light",
        "accent-dark",
        "accent-color"
        "accent-palette",
        "dark-mode",
        "light-mode",
        "system-theme",
        "color",
        "theme",
        "modern",
        "gui",
        "win32",
        "fluent",
        "sun-valley",
        "windows-11",
        "windows-10",
        "windows-8",
        "winui",
        "winaccent"
    ],
)
