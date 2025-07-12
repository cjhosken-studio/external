name = "gcc"

version = "11.2.0"

authors = [
    "GNU"
]

description = \
    """
    The gcc package contains the GNU Compiler Collection version 4.8.
    You'll need this package in order to compile C code.
    """

tools = [
    "gcc",
    "g++",
    "c++",
    "cpp",
    "gcc-ar",
    "gcc-ranlib",
    "gfortran",
    "gcc-nm",
    "gcov"
]

requires = [
    "cmake-3.31.7+",
]

def commands():
    env.PATH.append("{root}/bin")
    env.CC.set("{root}/bin/gcc")
    env.CXX.set("{root}/bin/g++")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.GCC_ROOT.set("{root}")