@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"


:: Debug output
echo Building nodejs %VERSION% for Windows...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%

:: Download nvm installer if it doesn't exist
if not exist "nvm-%VERSION%.exe" (
    echo Downloading nvm installer...
    curl -L https://github.com/coreybutler/nvm-windows/releases/download/1.2.2/nvm-setup.exe -o "nvm-%VERSION%.exe"
    if errorlevel 1 (
        echo ERROR: Failed to download nvm installer
        exit /b 1
    )
)

:: Install nvm
echo Installing nvm...
"nvm-%VERSION%.exe" /VERYSILENT /DIR=%REZ_BUILD_INSTALL_PATH%\\"nvm"
if errorlevel 1 (
    echo ERROR: nvm installation failed
    exit /b 1
)

echo Installing nodejs
"%REZ_BUILD_INSTALL_PATH%\\nvm\\nvm.exe" install %VERSION%
if errorlevel 1 (
    echo ERROR: nodejs installation failed
    exit /b 1
)

echo Successfully installed nodejs %VERSION%