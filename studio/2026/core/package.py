# @studio/platform-2026/package.py

name = "studio_core"
version = "2026.0"

description = \
    """
    The studio_core module contains common system and compile packages that all other packages should reference. This should be in line with the VFX Reference Platform.
    """

variants = [
    ["platform-linux", "arch-x86_64"]
]

requires = [
    # Compiler / Tooolchain Only
    "gcc-14.2",
    "cmake-3.31.7+",
    "python-3.13",
]

build_command = ""

def commands():
    # Shared C++20 setup
    env.CMAKE_CXX_STANDARD = "20"
    env.CXXFLAGS = "-std=c++20 -fPIC"