@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"


:: Debug output
echo Building Python %VERSION% for Windows...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%

:: Download Python installer if it doesn't exist
if not exist "python-%VERSION%-amd64.exe" (
    echo Downloading Python installer...
    curl -L https://www.python.org/ftp/python/%VERSION%/python-%VERSION%-amd64.exe -o "python-%VERSION%-amd64.exe"
    if errorlevel 1 (
        echo ERROR: Failed to download Python installer
        exit /b 1
    )
)

:: Install Python
echo Installing Python...
"python-%VERSION%-amd64.exe" /quiet InstallAllUsers=0 PrependPath=0 Include_test=0 TargetDir="%REZ_BUILD_INSTALL_PATH%"
if errorlevel 1 (
    echo ERROR: Python installation failed
    exit /b 1
)

:: Install numpy
echo Installing numpy...
"%REZ_BUILD_INSTALL_PATH%\\python.exe" -m pip install numpy==1.26.4
if errorlevel 1 (
    echo ERROR: Failed to install numpy
    exit /b 1
)

echo Successfully installed Python %VERSION%