name = "ptex"

version = "2.4.3"

authors = [
    "Walt Disney Animation Studios"
]

description = \
    """
    Ptex is a texture mapping system developed by Walt Disney Animation Studios for production-quality rendering:
        - No UV assignment is required! Ptex applies a separate texture to each face of a subdivision or polygon mesh.
        - The Ptex file format can efficiently store hundreds of thousands of texture images in a single file.
        - The Ptex API provides cached file I/O and high-quality filtering - everything that is needed to easily add Ptex support to a production-quality renderer or texture authoring application.
    """

tools = [

]

requires = [
    "cmake-3.31.7+",
    "gcc-11.2.0+"
]

def commands():
    env.PATH.append("{root}/bin")
    
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib64")

    env.Ptex_ROOT.set("{root}")
    env.Ptex_INCLUDE_DIR.set("{root}/include")
    env.Ptex_LIBRARY_DIR.set("{root}/lib64")