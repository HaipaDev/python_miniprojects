@echo off
setlocal enabledelayedexpansion

set "dragged_file=%~f1"
if "%dragged_file%"=="" (
    echo Please drag a file onto the bat file
) else (
    echo Compressing: !dragged_file!
    python "%~dp0/py_vidmuter.py" "!dragged_file!"
)
pause