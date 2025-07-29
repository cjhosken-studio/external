name = 'mpc'
version = '1.2.1'

description = 'GNU Project debugger.'

authors = ['GNU']

tools = []

variants = [
    ['platform-linux', 'arch-x86_64']
]

requires = [
    "gmp",
    "mpfr"
]

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.MPC_ROOT.set("{root}")
        env.MPC_LIBRARY_DIR.set("{root}/lib")
        env.MPC_INCLUDE_DIR.set("{root}/include")

build_command = "{root}/build.sh"