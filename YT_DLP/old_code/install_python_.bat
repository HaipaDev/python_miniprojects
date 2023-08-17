:: This file will try to install Python [3.11.4]
::powershell -command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe', 'C:/Programs/python-3.11.4.exe'); & c:\Programs\python-3.11.4.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 TargetDir=c:\Programs\Python311; [Environment]::SetEnvironmentVariable('PATH', ${env:path} + ';C:\Programs\Python311', 'Machine')"

@echo off
setlocal enabledelayedexpansion

:: Get the latest version of Python
for /f "tokens=2 delims=:" %%i in ('powershell -command "((Invoke-WebRequest -Uri 'https://www.python.org/downloads/windows/' -UseBasicParsing).Links | Where-Object href -like '*amd64.exe*').href"') do set "python_download_url=%%i"

:: Parse the version number from the download URL
for %%a in (!python_download_url!) do (
    set "download_url=%%~na"
    set "version=!download_url:~7,-6!"
)

:: Filter out alpha and beta versions
if "%version:~0,1%"=="3" (
    if "%version:~1,1%" geq "5" (
        if "%version:~1,1%" leq "9" (
            :: Download and install Python
            set "install_folder=C:\Programs\Python-!version!"
            powershell -command "(New-Object Net.WebClient).DownloadFile('%python_download_url%', 'C:/Programs/python-!version!.exe'); & c:\Programs\python-!version!.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 TargetDir=%install_folder%;"

            :: Add Python to PATH
            setx PATH "!install_folder!;!PATH!" /M

            echo Python version !version! installation completed.
        )
    )
)

pause