name = 'mpfr'
version = '4.1.0'

description = 'GNU Project debugger.'

authors = ['GNU']

tools = []

variants = [
    ['platform-linux', 'arch-x86_64']
]

requires = ["gmp"]

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.MPFR_ROOT.set("{root}")
        env.MPFR_LIBRARY_DIR.set("{root}/lib")
        env.MPFR_INCLUDE_DIR.set("{root}/include")

        env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")

build_command = "{root}/build.sh"