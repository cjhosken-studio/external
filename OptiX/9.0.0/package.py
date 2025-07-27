name = "optix"

version = "9.0.0"

authors = [
    "Academy Software Foundation"
]

description = \
    """
    An application framework for achieving optimal ray tracing performance on the GPU. It provides a simple, recursive, and flexible pipeline for accelerating ray tracing algorithms. Bring the power of NVIDIA GPUs to your ray tracing applications with programmable intersection, ray generation, and shading.
    """

tools = [

]

variants = [
    ["studio_core-2026"],
]

requires = [
]


def commands():
    import platform
    import os

    os.environ["OptiX_ROOT"] = "{root}"

    if platform.system() == "Windows":
        os.environ["OptiX_INCLUDE_DIR"] = "{root}\\include"
    else:
        os.environ["OptiX_INCLUDE_DIR"] = "{root}/include"

import platform

if platform.system() == "Windows":
    build_command = "{root}\\build.bat"
else:
    build_command = f"""
        set -e  # Exit immediately if any command fails

        # Create directories
        mkdir -p optix

        # Download with progress and fail if HTTP error
        echo "Downloading OptiX v{version}..."
        curl -L https://github.com/NVIDIA/optix-dev/archive/refs/tags/v{version}.tar.gz -o ./optix.tar.gz ||

        # Extract with error checking
        echo "Extracting archive..."
        tar -xzf optix.tar.gz -C optix --strip-components=1

        # Copy files
        echo "Installing to $REZ_BUILD_INSTALL_PATH..."
        cp -r optix/* "$REZ_BUILD_INSTALL_PATH/" ||
        # Clean up
        rm -rf optix optix.tar.gz

        echo "[REZ] OptiX-{version} installed successfully"
    """