name = "openexr"

version = "3.3.4"

authors = [
    "Academy Software Foundation"
]

description = \
    """
    OpenEXR provides the specification and reference implementation of the EXR file format, the professional-grade image storage format of the motion picture industry.
    """

tools = [
    "exr2aces",
    "exrenvmap",
    "exrheader",
    "exrinfo",
    "exrmakepreview",
    "exrmaketiled",
    "exrmanifest",
    "exrmetrics",
    "exrmultipart",
    "exrmultiview",
    "exrstdattr"
]

variants = [
    ["studio_core-2026"],
]

requires = [
    "pybind11-3",
    "imath-3"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")
    env.PYTHONPATH.append("{root}/python")

    env.OpenEXR_ROOT.set("{root}")
    env.OpenEXR_INCLUDE_DIR.set("{root}/include")
    env.OpenEXR_LIBRARY_DIR.set("{root}/lib64")
    
