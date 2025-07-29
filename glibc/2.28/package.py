name = "glibc"

version = "2.28"

authors = [
    "GNU"
]

description = \
    """
    The GNU C Library, commonly known as glibc, is the GNU Project implementation of the C standard library. 
    It provides a wrapper around the system calls of the Linux kernel and other kernels for application use. 
    """

requires = ["gcc-14"]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.glibc_ROOT.set("{root}")
        env.glibc_INCLUDE_DIR.set("{root}/include")
        env.glibc_LIBRARY_DIR.set("{root}/lib")


build_command = "{root}/build.sh"