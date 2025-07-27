@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"

:: Debug output
echo Building ffmpeg %VERSION% for Windows...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%

:: Download ffmpeg installer if it doesn't exist
if not exist "ffmpeg-%VERSION%.zip" (
    echo Downloading ffmpeg installer...
    curl -L https://github.com/GyanD/codexffmpeg/releases/download/%VERSION%/ffmpeg-%VERSION%-full_build.zip -o "ffmpeg-%VERSION%.zip"
    if errorlevel 1 (
        echo ERROR: Failed to download ffmpeg installer
        exit /b 1
    )
)

echo Installing ffmpeg...
tar -xzf "ffmpeg-%VERSION%.zip" --strip-components=1 -C "%REZ_BUILD_INSTALL_PATH%"
if errorlevel 1 (
    echo ERROR: ffmpeg installation failed
    exit /b 1
)

echo Successfully installed ffmpeg %VERSION%