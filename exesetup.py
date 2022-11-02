import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": [], "excludes": ["tkinter"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="8PuzzleV0.3",
    version="0.3",
    description="Sliding 8 Puzzle!",
    options={"build_exe": build_exe_options},
    executables=[Executable("8puzzleV0.3.py", base=base)],
)