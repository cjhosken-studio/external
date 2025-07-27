# @studio/platform-2026/package.py
import platform

name = "studio_core"
version = "2026.0"

description = \
    """
    The studio_core module contains common system and compile packages that all other packages should reference. This should be in line with the VFX Reference Platform.
    """

variants = []

requires = [
    # Compiler / Tooolchain Only
    "cmake-3.31.7+",
    "python-3.13",
]

if platform.system() == "Linux":
    requires += ["gcc-14.2"]
elif platform.system() == "Windows":
    requires += ["windows-2025"]

def commands():
    import platform
    import os
    
    # Set C++20 standard for all platforms
    os.environ["CMAKE_CXX_STANDARD"] = "20"
    
    # Platform-specific configurations
    if platform.system() == "Windows":
        # Windows-specific settings
        os.environ["CXXFLAGS"] = "/std:c++20 /EHsc /Zi"
        os.environ["CMAKE_GENERATOR"] = "Visual Studio 17 2022"  # Adjust version as needed
            
    else:
        # Unix-like systems (Linux, macOS)
        os.environ["CXXFLAGS"] = "-std=c++20 -fPIC"
        
        # Additional Unix flags
        if platform.system() == "Linux":
            os.environ["CXXFLAGS"] += " -Wall -Wextra"
        elif platform.system() == "Darwin":  # macOS
            os.environ["CXXFLAGS"] += " -stdlib=libc++"
    
    # Common compiler flags for all platforms
    os.environ["CMAKE_BUILD_TYPE"] = os.environ.get("CMAKE_BUILD_TYPE", "Release")
    
    # Optional: Set compiler explicitly if needed
    if "CXX" not in os.environ:
        if platform.system() == "Windows":
            os.environ["CXX"] = "cl.exe"
        else:
            os.environ["CXX"] = "g++"  # or clang++ if preferred

build_command = ""