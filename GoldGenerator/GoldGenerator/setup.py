import sys
from cx_Freeze import setup, Executable

setup(
    name = "GoldGenerator",
    version = "2.0",
    description = "GoldGenerator",
    executables = [Executable("GoldGenerator.py", base = "Win32GUI")])
