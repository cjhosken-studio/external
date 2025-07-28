@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"

:: Debug output
echo Building Visual Studio for Windows (with Windows SDK)...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%

:: Download git installer if it doesn't exist
if not exist "vs.exe" (
    echo Downloading Visual Studio installer...
    curl -L https://aka.ms/vs/17/release/vs_community.exe -o "vs.exe"
    if errorlevel 1 (
        echo ERROR: Failed to download Visual Studio installer
        exit /b 1
    )
)

:: Install Visual studio
echo Installing Visual Studio...
"vs.exe"
if errorlevel 1 (
    echo ERROR: Visual Studio installation failed
    exit /b 1
)

echo Successfully installed Visual Studio