name = "gcc"

version = "14.2.0"

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
    "gcc-nm",
    "gcov"
]

requires = [
    "gmp", "mpfr", "mpc"
]

variants = [
    ["platform-linux", "arch-x86_64"],
]

def commands():
    env.PATH.append("{root}/bin")
    env.CC.set("{root}/bin/gcc")
    env.CXX.set("{root}/bin/g++")
    env.LD_LIBRARY_PATH.prepend("{root}/lib:{root}/lib64")

    env.GCC_ROOT.set("{root}")

build_command = "{root}/build.sh"