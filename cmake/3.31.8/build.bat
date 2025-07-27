@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"


:: Debug output
echo Building CMake %VERSION% for Windows...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%

:: Download Python installer if it doesn't exist
if not exist "cmake-%VERSION%.zip" (
    echo Downloading CMake installer...
    curl -L https://github.com/Kitware/CMake/releases/download/v%VERSION%/cmake-%VERSION%-windows-x86_64.zip -o "cmake-%VERSION%.zip"
    if errorlevel 1 (
        echo ERROR: Failed to download CMake installer
        exit /b 1
    )
)

:: Install CMake
echo Installing CMake...
tar -xf "cmake-%VERSION%.zip" --strip-components=1 -C "%REZ_BUILD_INSTALL_PATH%"

echo Successfully installed CMake %VERSION%