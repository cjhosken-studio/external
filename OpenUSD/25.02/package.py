name = "usd"

version = "25.02"

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
    ["vfxplatform-2025"],
    ["vfxplatform-2026"]
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