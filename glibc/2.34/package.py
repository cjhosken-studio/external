name = "glibc"

version = "2.34"

authors = [
    "GNU"
]

description = \
    """
    """

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.glibc_ROOT.set("{root}")
        env.glibc_INCLUDE_DIR.set("{root}/include")
        env.glibc_LIBRARY_DIR.set("{root}/lib")


build_command = "{root}/build.sh"