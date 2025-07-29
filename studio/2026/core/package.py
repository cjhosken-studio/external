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
    "gcc-14.2",
    "cmake-3.31.7+",
    "python-3.13",
]

def commands():
    # Set C++20 standard for all platforms
    env.CMAKE_CXX_STANDARD.set("20")
    env.CXXFLAGS.set("-std=c++20 -fPIC -stdlib=libc++")
    env.CMAKE_BUILD_TYPE.set("Release")

build_command = ""