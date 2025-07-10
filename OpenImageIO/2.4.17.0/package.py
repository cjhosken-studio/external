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
    "cmake-4.0.3",
    "openexr-3.3.4",
    "python-3.13.5"
]

def commands():
    env.PATH.append("{root}/bin")
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib64")

    env.OpenImageIO_ROOT.append("{root}")
    env.OpenImageIO_INCLUDE_DIRS.append("{root}/include")
    env.OpenImageIO_LIBRARIES.append("{root}/lib64")


    env.OIIO_ROOT.set("{root}")
    env.OIIO_INCLUDE_DIRS.append("{root}/include")
    env.OIIO_LIBRARIES.append("{root}/lib64")