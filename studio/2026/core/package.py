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
    requires += ["windows"]

def commands():
    import platform
    import os
    
    # Set C++20 standard for all platforms
    env.CMAKE_CXX_STANDARD.set("20")
    
    # Platform-specific configurations
    if platform.system() == "Windows":
        # Windows-specific settings
        #os.environ["CXXFLAGS"] = "/std:c++20 /EHsc /Zi"
        os.environ["CMAKE_MODULE_PATH"] = "C:/opt/rez/Lib/site-packages/rezplugins/build_system/cmake_files"
        env.CMAKE_MODULE_PATH.set("C:/opt/rez/Lib/site-packages/rezplugins/build_system/cmake_files")
        env.CMAKE_GENERATOR.set("Visual Studio 17 2022")  # Adjust version as needed            
    else:
        # Unix-like systems (Linux, macOS)
        os.environ["CXXFLAGS"] = "-std=c++20 -fPIC"
        
        # Additional Unix flags
        if platform.system() == "Linux":
            os.environ["CXXFLAGS"] += " -Wall -Wextra"
        elif platform.system() == "Darwin":  # macOS
            os.environ["CXXFLAGS"] += " -stdlib=libc++"
    
    # Common compiler flags for all platforms
    env.CMAKE_BUILD_TYPE.set("Release")

build_command = ""