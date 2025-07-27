@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"


:: Debug output
echo Building git %VERSION% for Windows...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%

:: Download git installer if it doesn't exist
if not exist "git-%VERSION%.exe" (
    echo Downloading git installer...
    curl -L https://github.com/git-for-windows/git/releases/download/v%VERSION%.windows.1/Git-%VERSION%-64-bit.exe -o "git-%VERSION%.exe"
    if errorlevel 1 (
        echo ERROR: Failed to download git installer
        exit /b 1
    )
)

:: Install git
echo Installing git...
"git-%VERSION%.exe" /VERYSILENT
if errorlevel 1 (
    echo ERROR: git installation failed
    exit /b 1
)

echo Successfully installed git %VERSION%