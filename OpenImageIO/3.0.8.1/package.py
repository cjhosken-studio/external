name = "openimageio"

version = "3.0.8.1"

authors = [
    "Academy Software Foundation"
]

description = \
    """
    OpenImageIO is a toolset for reading, writing, and manipulating image files of any image file format relevant to VFX / animation via a format-agnostic API with a feature set, scalability, and robustness needed for feature film production.
    """

tools = [
    "iconvert",
    "idiff",
    "igrep",
    "iinfo",
    "maketx",
    "oiiotool",
    "testtex"
]

variants = [
    ["vfxbase-2026", "gcc-14.2", "python-3.13", "openexr-3.3+"],
]

requires = [
    "ptex-2.4",
    "pybind11",
]

def commands():
    env.PATH.append("{root}/bin")
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib64")

    env.PYTHONPATH.append("{root}/lib64/python3.9/site-packages")

    env.OpenImageIO_ROOT.set("{root}")
    env.OpenImageIO_INCLUDE_DIR.set("{root}/include")
    env.OpenImageIO_LIBRARY_DIR.set("{root}/lib64")