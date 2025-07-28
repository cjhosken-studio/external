name = "emscripten"

version = "4.0.8"

authors = [
    "Emscripten"
]

description = \
    """
    Emscripten is a complete compiler toolchain to WebAssembly, using LLVM, with a special focus on speed, size, and the Web platform.
    """

tools = []

def commands():
    env.EMSDK = "{root}"
    env.EM_CONFIG = "{root}/.emscripten"
    env.PATH.append("{root}")
    env.PATH.append("{root}/upstream/emscripten")
    env.PATH.append("{root}/node/22.16.0_64bit/bin")
    
    # Set other variables normally set by emsdk_env.sh
    env.EMSCRIPTEN = "{root}/emsdk/upstream/emscripten"
    env.LLVM_ROOT = "{root}/emsdk/upstream/bin"

import platform

if platform.system() == "Windows":
    build_command = ""
else:
    build_command = "{root}/build.sh"
