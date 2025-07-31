@echo off
setlocal enabledelayedexpansion

:: Python installer script for Rez
:: Installs Python to %REZ_BUILD_INSTALL_PATH%
:: Automatically detects version from parent folder name

:: Check if REZ_BUILD_INSTALL_PATH is set
if "%REZ_BUILD_INSTALL_PATH%"=="" (
    echo Error: REZ_BUILD_INSTALL_PATH is not set
    exit /b 1
)

for %%A in ("%~dp0.") do set "VERSION=%%~nxA"
:: Configuration
set PYTHON_URL=https://www.python.org/ftp/python/%VERSION%/python-%VERSION%-amd64.exe
set INSTALLER_NAME=python-%VERSION%-amd64.exe

echo Installing Python %VERSION% to %REZ_BUILD_INSTALL_PATH%

:: Create install directory if it doesn't exist
if not exist "%REZ_BUILD_INSTALL_PATH%" mkdir "%REZ_BUILD_INSTALL_PATH%"

:: Check if installer already exists
if exist "%INSTALLER_NAME%" (
    echo Using existing installer: %INSTALLER_NAME%
) else (
    :: Download Python installer
    echo Downloading Python installer...
    curl -L -o "%INSTALLER_NAME%" "%PYTHON_URL%"
    if errorlevel 1 (
        echo Failed to download Python installer
        echo URL: %PYTHON_URL%
        exit /b 1
    )
)

:: Install Python silently
echo Installing Python...
"%INSTALLER_NAME%" /quiet Include_test=0 TargetDir="%REZ_BUILD_INSTALL_PATH%"
if errorlevel 1 (
    echo Python installation failed
    exit /b 1
)

echo Python %VERSION% installed successfully to %REZ_BUILD_INSTALL_PATH%
exit /b 0