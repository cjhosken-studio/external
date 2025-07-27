@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"


:: Debug output
echo Building CUDA %VERSION% for Windows...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%

:: Download Python installer if it doesn't exist
if not exist "cuda-%VERSION%.exe" (
    echo Downloading CUDA installer...
    curl -L https://developer.download.nvidia.com/compute/cuda/%VERSION%/network_installers/cuda_%VERSION%_windows_network.exe -o "cuda-%VERSION%.exe"
    if errorlevel 1 (
        echo ERROR: Failed to download CUDA installer
        exit /b 1
    )
)

:: Install CUDA
echo Installing CUDA...
cuda-%VERSION%.exe -s --toolkit --defaultroot=%REZ_BUILD_INSTALL_PATH% --toolkitpath=%REZ_BUILD_INSTALL_PATH%

echo Successfully installed CUDA %VERSION%