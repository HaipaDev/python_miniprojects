::	Do not run this file by itself since it will not do anything without the variables from another file
::	But you can input your own url into these files and modify (a copy of) them however you want
::	Also by putting urls line by line in the inputurls.txt file they will succesively export automatically
::	And as it is said in the program you can put a timestamp for a snippet
::	formatted after the url like *01:03-01:37

@echo off
setlocal enabledelayedexpansion

:: Check if the file exists
if exist "inputurls.txt" (
    :: Check if the file is not empty
    for %%F in ("inputurls.txt") do (
        if %%~zF gtr 0 (
            echo Processing URLs from "inputurls.txt".
            
            for /f "usebackq tokens=*" %%a in ("inputurls.txt") do (
                set "url=%%a"
                echo Processing URL: !url!
                python "ytdlp_script.py" "!type!" "!url!"
            )
        ) else (
            python "ytdlp_script.py" "!type!" "!url!"
        )
    )
) else (
    python "ytdlp_script.py" "!type!" "!url!"
)
::if "%url%"=="" pause