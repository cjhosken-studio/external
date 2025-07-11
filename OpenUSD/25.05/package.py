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

requires = [
    "cmake-4.0.3",
    "opensubdiv-3.6.1",
    "opencolorio-2.4.2",
    "openimageio-2.4.17.0",
    "materialx-1.39.3",
    "ptex-2.4.3",
    "python-3.13.5",
    'onetbb-2022.2.0'
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