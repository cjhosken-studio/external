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

]

requires = [
    "cmake-4.0.3",
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")

    env.OpenEXR_ROOT.append("{root}")
    
