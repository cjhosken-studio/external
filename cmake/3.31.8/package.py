import platform

name = "cmake"
version = "3.31.8"

variants = []

build_requires = []

tools = ["cmake", "cmake-gui", "cmcldeps", "cpack", "ctest"]

def commands():
    import platform
    import os

    if platform.system() == "Windows":
        os.environ["PATH"] = "{root}\\bin;" + os.environ.get("PATH")
        os.environ["CMAKE_PREFIX_PATH"] += ";{root}\\share\\cmake-3.31"
    else:
        os.environ["PATH"] = "{root}/bin;" + os.environ.get("PATH")
        os.environ["CMAKE_PREFIX_PATH"] += ";{root}/share/cmake-3.31"

if platform.system() == "Windows":
    build_command = "{root}\\build.bat"
else:
    build_command = f"""
    set -e
    wget https://github.com/Kitware/CMake/releases/download/v{version}/cmake-{version}.tar.gz -O cmake_src.tar.gz
    tar -xzf cmake_src.tar.gz
    cd cmake-{version}
    ./bootstrap --prefix=$REZ_BUILD_INSTALL_PATH \\
                --parallel=$NPROC \\
                --system-curl \\
                --no-qt-gui
    make -j$NPROC
    make install
    """
