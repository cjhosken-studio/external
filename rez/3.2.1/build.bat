@echo off
setlocal enabledelayedexpansion

:: Rez Installer for Windows
echo === Rez Installer ===

:: Get script directory
for /f "delims=" %%I in ("%0") do set SCRIPT_DIR=%%~dpI
set "VERSION=%SCRIPT_DIR:~0,-1%"
for %%I in ("%VERSION%") do set "VERSION=%%~nxI"
set "BUILD_DIR=%SCRIPT_DIR%build"
set "HOME=%USERPROFILE%"
set "BASHRC_FILE=%HOME%\.bashrc"
set "REZ_BIN_PATH=C:\opt\rez\Scripts\rez"
set "REZ_COMPLETE_PATH=C:\opt\rez\completion\complete"

echo Version: %VERSION%
echo Build directory: %BUILD_DIR%

:: Create build directory
if not exist "%BUILD_DIR%" mkdir "%BUILD_DIR%"
cd /d "%BUILD_DIR%"

:: Download the package
echo Downloading Rez %VERSION%...
set "DOWNLOAD_URL=https://github.com/AcademySoftwareFoundation/rez/archive/refs/tags/%VERSION%.tar.gz"
curl -L -o "%VERSION%.tar.gz" "%DOWNLOAD_URL%"
if %errorlevel% neq 0 (
    echo Error: Failed to download Rez %VERSION% 1>&2
    exit /b 1
)

:: Extract the package
echo Extracting package...
tar -xzf "%VERSION%.tar.gz"
if %errorlevel% neq 0 (
    echo Error: Failed to extract package 1>&2
    exit /b 1
)

:: Find the extracted directory
set "EXTRACTED_DIR="
for /d %%I in ("%BUILD_DIR%\rez-%VERSION%*") do (
    set "EXTRACTED_DIR=%%I"
    goto :found_dir
)
:found_dir
if not defined EXTRACTED_DIR (
    echo Error: Could not find extracted Rez directory 1>&2
    exit /b 1
)

:: Run install script with admin privileges if needed
echo Installing Rez...
if exist "%EXTRACTED_DIR%\install.py" (
    :: Check for admin privileges
    net session >nul 2>&1
    if %errorlevel% neq 0 (
        echo Requesting admin privileges for installation...
        powershell -command "Start-Process python -ArgumentList '%EXTRACTED_DIR%\install.py' -Verb RunAs"
    ) else (
        python "%EXTRACTED_DIR%\install.py"
    )
) else (
    echo Error: install.py not found in %EXTRACTED_DIR% 1>&2
    exit /b 1
)

echo.
echo SUCCESS! Rez %VERSION% has been installed.
echo.
echo To start using Rez, please add C:/opt/rez/Scripts/rez to PATH.
echo Then, run rez-bind os

endlocal