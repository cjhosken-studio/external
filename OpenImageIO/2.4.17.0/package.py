name = "openimageio"

version = "2.4.17.0"

authors = [
    "Academy Software Foundation"
]

description = \
    """
    OpenImageIO is a toolset for reading, writing, and manipulating image files of any image file format relevant to VFX / animation via a format-agnostic API with a feature set, scalability, and robustness needed for feature film production.
    """

tools = [

]

requires = [
    "openexr-3.3+",
    "python-3.11+",
    "opencolorio-2.4+",
    "ptex-2.4+"
]

def commands():
    env.PATH.append("{root}/bin")
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib64")

    env.OpenImageIO_ROOT.set("{root}")
    env.OpenImageIO_INCLUDE_DIR.set("{root}/include")
    env.OpenImageIO_LIBRARY_DIR.set("{root}/lib64")