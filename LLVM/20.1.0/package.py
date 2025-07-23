name = "llvm"

version = "20.1.0"

authors = [
    ""
]

description = \
    """
    """

variants = [
    ["platform-linux", "arch-x86_64"],
]

requires = [
]

tools = [

    ]

build_command = \
    f"""
    set -e
    wget https://github.com/llvm/llvm-project/releases/download/llvmorg-{version}/LLVM-{version}-Linux-X64.tar.xz
    tar -xf LLVM-{version}-Linux-X64.tar.xz
    cp -r LLVM-{version}-Linux-X64/* $REZ_BUILD_INSTALL_PATH
    """

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_MODULE_PATH.append("{root}/lib/cmake")

    env.LLVM_ROOT.set("{root}")
    env.LLVM_INCLUDE_DIR.set("{root}/include")
    env.LLVM_LIBRARY_DIR.set("{root}/lib")

