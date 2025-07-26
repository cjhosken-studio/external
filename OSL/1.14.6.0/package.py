name = "osl"

version = "1.14.6.0"

authors = [
    "Academy Software Foundation"
]

description = \
    """
    Open Shading Language (OSL) is a small but rich language for programmable shading in advanced renderers and other applications, ideal for describing materials, lights, displacement, and pattern generation.
    """

tools = [

]

variants = [
    ["studio_core-2026", "python-3.13"]
]

requires = [
    "openimageio-3",
    "llvm-20",
    "imath-3",
    "optix-7+",
    "cuda-11+",
    "pybind11-2.7+",
    "qt-6.8"
]

def commands():
    env.PATH.append("{root}/bin")
    
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib64")

    env.OSL_ROOT.set("{root}")
    env.OSL_INCLUDE_DIR.set("{root}/include")
    env.OSL_LIBRARY_DIR.set("{root}/lib64")