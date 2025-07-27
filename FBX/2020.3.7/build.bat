@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"


set "VERSION_NO_DOTS=%VERSION:.=%"


:: Debug output
echo Building FBX %VERSION% for Windows...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%

:: Download FBX installer if it doesn't exist
if not exist "fbx-%VERSION%.exe" (
    echo Downloading Python installer...
    curl -L https://damassets.autodesk.net/content/dam/autodesk/www/files/fbx%VERSION_NO_DOTS%_fbxsdk_vs2022_win.exe -o "fbx-%VERSION%.exe"
    if errorlevel 1 (
        echo ERROR: Failed to download FBX installer
        exit /b 1
    )
)

:: Install FBX
echo Installing FBX...
echo Please use the default install path!
"fbx-%VERSION%.exe"

echo Successfully installed FBX %VERSION%