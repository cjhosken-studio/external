name = "cmake"
version = "3.31.8"

variants = [
    ["platform-linux", "arch-x86_64"],
    ["platform-windows", "arch-x86_64"],
    ["platform-osx", "arch-arm64"]
]

build_requires = []

tools = ["cmake", "ctest", "cpack"]

def commands():
    env.PATH.prepend("{root}/bin")
    if building:
        env.CMAKE_PREFIX_PATH = "{root}/share/cmake-3.31"

build_command = \
    f"""
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
