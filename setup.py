from setuptools import setup, find_packages

description = open("README.md", "r").read()

setup(
    name = "winaccent",
    version = "0.1",
    license = "MIT",
    author = "Valer100",
    description = "A simple module for getting Windows' accent color",
    url = "https://github.com/Valer100/winaccent",
    project_urls = {
        "Source": "https://github.com/Valer100/winaccent",
        "Issues": "https://github.com/Valer100/winaccent/issues",
    },
    packages = find_packages(),
    install_requires = [
        "darkdetect"
    ],
    long_description = description,
    long_description_content_type = "text/markdown",
    classifiers = [
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
        "Operating System :: Windows 10",
        "Operating System :: Windows 11",
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
    ],
)
