@echo off
pip install setuptools wheel twine
rmdir /q /s dist
python setup.py sdist bdist_wheel
twine upload dist/*
rmdir /q /s dist
rmdir /q /s build
rmdir /q /s sv_ttk_colorizer.egg-info
