@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"


:: Debug output
echo Building OneAPI %VERSION% for Windows...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%

:: Download OneAPI installer if it doesn't exist
if not exist "oneapi-%VERSION%.exe" (
    echo Downloading Python installer...
    curl -L https://registrationcenter-download.intel.com/akdlm/IRC_NAS/09a8acaf-265f-4460-866c-a3375ed5b4ff/intel-oneapi-base-toolkit-%VERSION%.591_offline.exe -o "oneapi-%VERSION%.exe"
    if errorlevel 1 (
        echo ERROR: Failed to download OneAPI installer
        exit /b 1
    )
)

:: Install OneAPI
echo Installing OneAPI...
"oneapi-%VERSION%.exe" -s -a --silent --eula accept --action install
if errorlevel 1 (
    echo ERROR: OneAPI installation failed
    exit /b 1
)

echo Successfully installed OneAPI %VERSION%
