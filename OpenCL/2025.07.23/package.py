name = "opencl"

version = "2025.07.23"

authors = [
    "Khronos Group"
]

description = \
    """
    This is the Khronos OpenCL SDK. It brings together all the components needed to develop OpenCL applications:
    """

tools = [
    "clinfo",
    "cllayerinfo"
]

variants = [
    ["studio_core-2026"]
]

requires = [
    "git",
]

def commands():
    env.PATH.append("{root}/bin")
    
    env.CMAKE_MODULE_PATH.append("{root}/share/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib64")

    env.OpenCL_ROOT.set("{root}")
    env.OpenCL_INCLUDE_DIR.set("{root}/include")
    env.OpenCL_LIBRARY_DIR.set("{root}/lib64")