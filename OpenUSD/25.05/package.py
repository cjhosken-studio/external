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
    
    "python-3.13.5"
]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.PXR_PLUGINPATHNAME.append("{root}/plugin/usd")
    env.pxr_ROOT.append("{root}")