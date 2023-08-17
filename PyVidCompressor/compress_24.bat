@echo off
setlocal enabledelayedexpansion

set "dragged_file=%~f1"
if "%dragged_file%"=="" (
    echo Please drag a file onto the bat file
) else (
	set "target_size=24"
	
    echo Compressing: !dragged_file! to !target_size!MB
    python "%~dp0/py_vidcompressor.py" "!dragged_file!" !target_size!
)
pause