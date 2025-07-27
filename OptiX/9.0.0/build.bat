@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"


:: Debug output
echo Building OptiX %VERSION% for Windows...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%

:: Download OptiX installer if it doesn't exist
if not exist "optix-%VERSION%.tar.gz" (
    echo Downloading OptiX installer...
    curl -L https://github.com/NVIDIA/optix-dev/archive/refs/tags/v9.0.0.tar.gz -o "optix-%VERSION%.tar.gz"
    if errorlevel 1 (
        echo ERROR: Failed to download OptiX installer
        exit /b 1
    )
)

:: Install OptiX
echo Installing OptiX...
tar -xzf "optix-%VERSION%.tar.gz" --strip-components=1 -C "%REZ_BUILD_INSTALL_PATH%"
if errorlevel 1 (
    echo ERROR: OptiX installation failed
    exit /b 1
)

echo Successfully installed OptiX %VERSION%