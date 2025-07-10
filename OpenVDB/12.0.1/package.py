name = "openvdb"

version = "12.0.1"

authors = [
    "Academy Software Foundation"
]

description = \
    """
    OpenVDB is an open source C++ library comprising a novel hierarchical data structure and a large suite of tools for the efficient storage and manipulation of sparse volumetric data discretized on three-dimensional grids. 
    It was developed by DreamWorks Animation for use in volumetric applications typically encountered in feature film production.
    """

tools = [

]

requires = [
    "cmake-4.0.3",
    "boost-1.88.0"
]

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.OpenVDB_ROOT.append("{root}")