name = 'gmp'
version = '6.2.1'

description = 'GNU Project debugger.'

authors = ['GNU']

tools = []

variants = [
    ['platform-linux', 'arch-x86_64']
]

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.GMP_ROOT.set("{root}")
        env.GMP_LIBRARY_DIR.set("{root}/lib")
        env.GMP_INCLUDE_DIR.set("{root}/include")

        env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")

build_command = "{root}/build.sh"