name = "usd"

version = "25.05"

authors = [
    "Pixar Animation Studios"
]

description = \
    """
    Universal Scene Description (USD) is an efficient, scalable system for authoring, reading, and streaming time-sampled scene description for interchange between graphics applications.
    """



tools = [
    
]

variants = [
    ["vfxbase-2026", "gcc-14.2", "python-3.13", "opencolorio-2.4", "ptex-2.4", "opensubdiv-3.6"],
]

requires = [
    "openimageio"
]

def commands():
    env.PATH.append("{root}")
    env.PYTHONPATH.append("{root}/python")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.PXR_PLUGINPATHNAME.append("{root}/plugin/usd")

    env.USD_ROOT.set("{root}")
    env.USD_INCLUDE_DIR.set("{root}/include")
    env.USD_LIBRARY_DIR.set("{root}/lib")